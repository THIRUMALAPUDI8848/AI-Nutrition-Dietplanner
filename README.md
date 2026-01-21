# 🏥 AI Health Companion

A personalized nutrition and wellness assistant powered by Google's Gemini AI. Get custom meal plans, food analysis, and expert health insights tailored to your unique profile.

##  Features

###  Personalized Meal Planning
- Generate custom meal plans (3, 7, or 14 days)
- Nutritional breakdowns with macros and calories
- Shopping lists organized by category
- Meal prep tips and time estimates
- Alternative meal options for variety

###  Food Analysis
- Upload food photos for instant analysis
- Detailed nutritional breakdown
- Calorie and macro estimation
- Health impact assessment based on your profile
- Personalized recommendations and modifications

###  Health Insights
- Ask any nutrition or health question
- Context-aware responses using your health profile
- Science-backed explanations
- Actionable steps and recommendations
- Chat history tracking

###  Personal Health Profile
- Track health goals and fitness routines
- Record medical conditions and dietary restrictions
- Store food preferences
- All recommendations personalized to YOUR profile

##  Getting Started

### Prerequisites

- Python 3.8 or higher (3.13.11)
- Google Gemini API key (free tier available)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd ai-health-companion
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Create a new API key (free tier available)
   - Copy your API key

4. **Configure your API key** (Choose one method)

   **Method A: Using .env file (Recommended)**
   - Create a `.env` file in the project root:
     ```bash
     echo "GOOGLE_API_KEY=your_api_key_here" > .env
     ```
   
   **Method B: Direct in code**
   - Open the Python file and add your key:
     ```python
     GOOGLE_API_KEY = "your_api_key_here"
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

##  Usage Guide

### Setting Up Your Profile

1. **Open the sidebar** (click `>` if collapsed)
2. **Fill in your health information:**
   - Health Goals (e.g., "Lose 15 pounds in 4 months")
   - Medical Conditions (if any)
   - Current Fitness Routines
   - Food Preferences (Vegetarian, Vegan, etc.)
   - Dietary Restrictions (allergies, intolerances)
3. **Click "Update Profile"** to save

### Generating Meal Plans

1. Go to **"🍽️ Meal Planning"** tab
2. Describe specific requirements (optional)
3. Select meal plan duration (3, 7, or 14 days)
4. Click **"Generate Meal Plan"**
5. Download your plan as a text file for reference

### Analyzing Food

1. Go to **"📸 Food Analysis"** tab
2. Upload a clear photo of your meal
3. Choose analysis type:
   - **Quick Analysis**: Fast overview
   - **Detailed Breakdown**: Complete nutrition info
   - **Health Impact**: Personalized to your profile
4. Click **"Analyze Food"**
5. Save the analysis for your records

### Getting Health Insights

1. Go to **" Health Insights"** tab
2. Type your health or nutrition question
3. Toggle "Use my profile" for personalized answers
4. Click **"Get Expert Insights"**
5. View your recent questions in the chat history

##  Configuration

### API Key Security

**Never commit your API key to version control!**

Add `.env` to your `.gitignore`:
```
.env
__pycache__/
*.pyc
.streamlit/
```

### Customization

- **Cache Duration**: Modify `@st.cache_data(ttl=3600)` to change caching time
- **Model Selection**: Change `gemini-2.0-flash-exp` to other Gemini models
- **Page Layout**: Adjust `layout="wide"` in `st.set_page_config()`

##  Requirements

```
streamlit==1.31.0
google-generativeai==0.3.2
python-dotenv==1.0.0
Pillow==10.2.0
```

##  Troubleshooting

### "API quota exceeded" error
- You've hit the free tier limit
- Wait for quota reset or upgrade your API plan
- Check usage at [Google AI Studio](https://aistudio.google.com/)

### "Invalid API key" error
- Verify your API key is correct
- Ensure no extra spaces in `.env` file
- Try regenerating your API key

### Images not uploading
- Ensure file is JPG, JPEG, or PNG format
- Check file size (keep under 4MB)
- Verify image is not corrupted

### App not loading
- Check if port 8501 is available
- Try: `streamlit run app.py --server.port 8502`
- Verify all dependencies are installed

##  Important Disclaimers

- This AI assistant provides **general health information only**
- **Not a substitute for professional medical advice**
- Always consult healthcare professionals for medical decisions
- AI responses may occasionally contain errors
- Nutritional values are estimates

##  Best Practices

1. **Keep your profile updated** for accurate recommendations
2. **Be specific** in your questions and requirements
3. **Use clear, well-lit photos** for food analysis
4. **Download important plans** for offline reference
5. **Review AI suggestions** with critical thinking

##  Privacy & Data

- All data stored locally in session state
- No data sent to external servers (except Gemini API calls)
- Chat history cleared when you close the browser
- Profile data not persisted between sessions

##  License

This project is for educational and personal use. Please comply with Google's Gemini API Terms of Service.

##  Contributing

Suggestions and improvements welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share feedback

##  Support

For issues with:
- **The app**: Check troubleshooting section above
- **Gemini API**: Visit [Google AI documentation](https://ai.google.dev/docs)
- **Streamlit**: Check [Streamlit docs](https://docs.streamlit.io)

---

**Made with  using Streamlit and Google Gemini AI**