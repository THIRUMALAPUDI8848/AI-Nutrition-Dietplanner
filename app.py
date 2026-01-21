from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import time

# Configure Gemini - Use environment variable for security
GOOGLE_API_KEY= "AIzaSyAsZCETPZc0EP8obYGIebuynjJ-RoQk_Tg"  # AIzaSyDLKYdVg0MqT2gPPwdo-8Cr950_7JOai1U insert your Gemini API key https://aistudio.google.com/apikey
genai.configure(api_key=GOOGLE_API_KEY)



# Initialize session state
def initialize_session_state():
    if 'health_profile' not in st.session_state:
        st.session_state.health_profile = {
            'goals': 'Lose 15 pounds in 4 months\nMaintain fitness',
            'conditions': 'None',
            'routines': '30-minute walk daily',
            'preferences': 'Vegetarian\nNon-Veg',
            'restrictions': 'No Junk Food'
        }
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'last_meal_plan' not in st.session_state:
        st.session_state.last_meal_plan = None

initialize_session_state()

# Function to get Gemini response 

def get_gemini_response(input_prompt, image_data=None):
    model = genai.GenerativeModel('gemini-2.5-flash')

    content = [input_prompt]

    if image_data:
        content.extend(image_data)

    try:
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
        

def input_image_setup(uploaded_file):
    """Process uploaded image for Gemini"""
    if uploaded_file is not None:
        try:
            bytes_data = uploaded_file.getvalue()
            image_parts = [{
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }]
            return image_parts
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None
    return None

def validate_profile(profile):
    """Check if health profile has meaningful data"""
    return any(
        value and value.strip() and value.strip().lower() != 'none' 
        for value in profile.values()
    )

# App layout
st.set_page_config(
    page_title="AI Health Companion", 
    layout="wide",
    page_icon="🏥"
)

st.title("🏥 AI Health Companion")
st.markdown("*Your personalized nutrition and wellness assistant powered by AI*")

# Sidebar for health profile
with st.sidebar:
    st.header("👤 Your Health Profile")
    
    with st.form("health_profile_form"):
        health_goals = st.text_area(
            "🎯 Health Goals",
            value=st.session_state.health_profile['goals'],
            help="What do you want to achieve?"
        )
        
        medical_conditions = st.text_area(
            "🏥 Medical Conditions",
            value=st.session_state.health_profile['conditions'],
            help="Any health conditions we should know about?"
        )
        
        fitness_routines = st.text_area(
            "💪 Fitness Routines",
            value=st.session_state.health_profile['routines'],
            help="Your current exercise habits"
        )
        
        food_preferences = st.text_area(
            "🍽️ Food Preferences",
            value=st.session_state.health_profile['preferences'],
            help="What types of food do you prefer?"
        )
        
        restrictions = st.text_area(
            "🚫 Dietary Restrictions",
            value=st.session_state.health_profile['restrictions'],
            help="Any foods you must avoid?"
        )
        
        submitted = st.form_submit_button("💾 Update Profile", use_container_width=True)
        
        if submitted:
            st.session_state.health_profile = {
                'goals': health_goals,
                'conditions': medical_conditions,
                'routines': fitness_routines,
                'preferences': food_preferences,
                'restrictions': restrictions
            }
            st.success("✅ Profile updated successfully!")
            st.cache_data.clear()  # Clear cache when profile changes
            time.sleep(0.5)
            st.rerun()
    
    st.divider()
    st.caption("💡 Tip: Keep your profile updated for better recommendations")

# Main content area
tab1, tab2, tab3, tab4 = st.tabs([
    "🍽️ Meal Planning", 
    "📸 Food Analysis", 
    "💡 Health Insights",
    "📊 Profile Summary"
])

with tab1:
    st.header("Personalized Meal Planning")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Your Current Needs")
        user_input = st.text_area(
            "Describe specific requirements:",
            placeholder="e.g., 'I need quick meals under 30 minutes' or 'High protein meals for muscle gain'",
            height=100
        )
        
        meal_duration = st.selectbox(
            "Meal plan duration:",
            ["3 days", "7 days", "14 days"],
            index=1
        )
    
    with col2:
        st.subheader("📋 Quick View")
        if validate_profile(st.session_state.health_profile):
            st.success("✅ Profile Complete")
            with st.expander("View Profile"):
                for key, value in st.session_state.health_profile.items():
                    st.text(f"{key.title()}: {value[:50]}...")
        else:
            st.warning("⚠️ Complete your profile")
    
    if st.button("🎨 Generate Meal Plan", use_container_width=True, type="primary"):
        if not validate_profile(st.session_state.health_profile):
            st.error("❌ Please complete your health profile in the sidebar first")
        else:
            with st.spinner("🔮 Creating your personalized meal plan..."):
                prompt = f"""
                Create a personalized {meal_duration} meal plan based on this health profile:

                Health Goals: {st.session_state.health_profile['goals']}
                Medical Conditions: {st.session_state.health_profile['conditions']}
                Fitness Routines: {st.session_state.health_profile['routines']}
                Food Preferences: {st.session_state.health_profile['preferences']}
                Dietary Restrictions: {st.session_state.health_profile['restrictions']}
                
                Additional Requirements: {user_input if user_input else "None"}

                Provide:
                1. Complete meal plan with breakfast, lunch, dinner, and 2 snacks per day
                2. Daily nutritional breakdown (calories, protein, carbs, fats, fiber)
                3. Why each meal aligns with their goals
                4. Organized shopping list by category
                5. Meal prep tips and time estimates
                6. Alternative options for variety

                Format with clear headings, bullet points, and emojis for readability.
                """

                response = get_gemini_response(prompt)
                st.session_state.last_meal_plan = response
                
                st.success("✅ Meal plan generated!")
                st.divider()
                st.markdown(response)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="📥 Download as Text",
                        data=response,
                        file_name=f"meal_plan_{meal_duration.replace(' ', '_')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                with col2:
                    if st.button("🔄 Regenerate", use_container_width=True):
                        st.cache_data.clear()
                        st.rerun()

with tab2:
    st.header("Food Analysis")
    st.markdown("Upload a photo of your meal for detailed nutritional analysis")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "📸 Upload food image",
            type=["jpg", "jpeg", "png"],
            help="Take a clear photo of your meal"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Your Food", use_column_width=True)
    
    with col2:
        if uploaded_file is not None:
            analysis_type = st.radio(
                "Analysis Type:",
                ["Quick Analysis", "Detailed Breakdown", "Health Impact"],
                help="Choose the depth of analysis"
            )
            
            if st.button("🔍 Analyze Food", use_container_width=True, type="primary"):
                with st.spinner("🔬 Analyzing your food..."):
                    image_data = input_image_setup(uploaded_file)
                    
                    if image_data:
                        if analysis_type == "Quick Analysis":
                            prompt = """Analyze this food image and provide:
                            - Food identification
                            - Estimated calories
                            - Quick macro breakdown (protein, carbs, fats)
                            - One health tip"""
                        elif analysis_type == "Detailed Breakdown":
                            prompt = """Provide comprehensive food analysis:
                            - Detailed ingredient identification
                            - Calorie count with breakdown
                            - Complete macro and micronutrient profile
                            - Portion size recommendations
                            - Preparation method analysis"""
                        else:
                            prompt = f"""Analyze this food considering the user's profile:
                            {st.session_state.health_profile}
                            
                            Provide:
                            - Nutritional analysis
                            - How it aligns with their health goals
                            - Potential benefits or concerns
                            - Suggested modifications
                            - Better alternatives if needed"""
                        
                        response = get_gemini_response(prompt, image_data)
                        
                        st.divider()
                        st.subheader("📊 Analysis Results")
                        st.markdown(response)
                        
                        st.download_button(
                            "💾 Save Analysis",
                            response,
                            "food_analysis.txt",
                            use_container_width=True
                        )
        else:
            st.info("👆 Upload an image to start analysis")

with tab3:
    st.header("Health Insights & Expert Advice")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        health_query = st.text_input(
            "🤔 Ask any health/nutrition question:",
            placeholder="e.g., 'How can I boost my energy levels naturally?'"
        )
    
    with col2:
        context_aware = st.checkbox(
            "Use my profile",
            value=True,
            help="Get personalized answers based on your health profile"
        )
    
    if st.button("🧠 Get Expert Insights", use_container_width=True, type="primary"):
        if not health_query:
            st.warning("⚠️ Please enter a question")
        else:
            with st.spinner("🔍 Researching your question..."):
                if context_aware:
                    prompt = f"""
                    As a certified nutritionist and health expert, answer this question:
                    "{health_query}"
                    
                    Consider the user's health profile:
                    Goals: {st.session_state.health_profile['goals']}
                    Conditions: {st.session_state.health_profile['conditions']}
                    Fitness: {st.session_state.health_profile['routines']}
                    Preferences: {st.session_state.health_profile['preferences']}
                    Restrictions: {st.session_state.health_profile['restrictions']}
                    
                    Provide:
                    1. Clear, science-backed explanation
                    2. Personalized recommendations for THIS user
                    3. Actionable steps they can take today
                    4. Any precautions specific to their profile
                    5. Relevant foods/supplements
                    
                    Use simple language with examples.
                    """
                else:
                    prompt = f"""
                    As a certified nutritionist, provide comprehensive insights about:
                    "{health_query}"
                    
                    Include:
                    1. Scientific explanation
                    2. General recommendations
                    3. Practical action steps
                    4. Common precautions
                    5. Food/supplement suggestions
                    
                    Keep it clear and actionable.
                    """
                
                response = get_gemini_response(prompt)
                
                st.success("✅ Research complete!")
                st.divider()
                st.markdown(response)
                
                # Add to chat history
                st.session_state.chat_history.append({
                    'question': health_query,
                    'answer': response
                })
                
                st.download_button(
                    "💾 Save Insights",
                    response,
                    "health_insights.txt",
                    use_container_width=True
                )
    
    if st.session_state.chat_history:
        st.divider()
        st.subheader("📚 Recent Questions")
        for idx, item in enumerate(reversed(st.session_state.chat_history[-5:])):
            with st.expander(f"Q: {item['question'][:60]}..."):
                st.markdown(item['answer'])

with tab4:
    st.header("Profile Summary & Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Your Profile")
        st.json(st.session_state.health_profile)
    
    with col2:
        st.subheader("📈 Activity")
        st.metric("Questions Asked", len(st.session_state.chat_history))
        st.metric("Meal Plans Generated", 1 if st.session_state.last_meal_plan else 0)
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.success("✅ History cleared!")
            st.rerun()
    
    st.divider()
    st.subheader("💡 Pro Tips")
    st.info("""
    - **Update regularly**: Keep your profile current for best results
    - **Be specific**: Detailed questions get better answers
    - **Use images**: Food analysis works best with clear, well-lit photos
    - **Save plans**: Download meal plans for offline reference
    """)

# Footer
st.divider()
st.caption("⚠️ Disclaimer: This AI assistant provides general health information. Always consult healthcare professionals for medical advice.")