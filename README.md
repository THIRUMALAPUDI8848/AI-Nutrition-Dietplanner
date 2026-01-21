# 🏥 AI Health Companion

> **Your personalized nutrition and wellness assistant powered by Google Gemini 2.5 Flash AI**

Transform your health journey with AI-powered meal planning, instant food analysis, and personalized nutrition advice tailored to your unique health profile.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🌟 Features Overview

### 🍽️ **Smart Meal Planning**
Create personalized meal plans that actually fit your lifestyle:
- **Flexible Duration**: 3, 7, or 14-day meal plans
- **Complete Daily Menus**: Breakfast, lunch, dinner + 2 healthy snacks
- **Nutritional Tracking**: Full breakdown of calories, protein, carbs, fats, and fiber
- **Smart Shopping Lists**: Organized by category for efficient grocery shopping
- **Time-Saving Tips**: Meal prep guidance with time estimates
- **Variety Built-In**: Alternative options to prevent meal fatigue
- **Goal-Aligned**: Every meal designed to support YOUR specific health goals

### 📸 **AI Food Analysis**
Turn your phone camera into a nutrition expert:
- **Instant Analysis**: Upload food photos for immediate nutritional breakdown
- **Three Analysis Modes**:
  - 🚀 **Quick Analysis**: 30-second overview with calories and macros
  - 🔬 **Detailed Breakdown**: Complete nutritional profile with micronutrients
  - 🎯 **Health Impact**: Personalized assessment based on YOUR health profile
- **Smart Recognition**: Identifies ingredients and portion sizes
- **Actionable Insights**: Get suggestions for healthier alternatives
- **Save Results**: Download analyses for tracking and reference

### 💡 **Expert Health Insights**
Your 24/7 nutrition consultant:
- **Ask Anything**: Get answers to any health or nutrition question
- **Context-Aware**: AI considers YOUR health profile for personalized advice
- **Science-Backed**: Responses based on current nutritional science
- **Actionable Steps**: Clear, practical recommendations you can implement today
- **Chat History**: Track all your questions and answers
- **Download Advice**: Save insights as text files for future reference

### 👤 **Personal Health Profile**
All recommendations tailored to YOU:
- 🎯 **Health Goals**: Weight loss, muscle gain, maintenance, or wellness
- 🏥 **Medical Conditions**: Diabetes, hypertension, allergies, etc.
- 💪 **Fitness Routines**: Current exercise habits and activity level
- 🍽️ **Food Preferences**: Vegetarian, vegan, keto, Mediterranean, etc.
- 🚫 **Dietary Restrictions**: Allergies, intolerances, religious restrictions
- 🔄 **Easy Updates**: Modify your profile anytime as your needs change

---

## 🎬 Quick Start (5 Minutes)

### Prerequisites Checklist
- ✅ Python 3.8 or higher installed
- ✅ Internet connection
- ✅ Google Gemini API key (get free at [aistudio.google.com](https://aistudio.google.com/apikey))

### Installation Steps

**1️⃣ Download the Project**
```bash
# Clone the repository
git clone <your-repository-url>
cd ai-health-companion

# OR download and extract the ZIP file
```

**2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**3️⃣ Get Your Free API Key**
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your key (starts with `AIza...`)

**4️⃣ Add Your API Key**

Open the Python file and find this line:
```python
GOOGLE_API_KEY = "AIzaSyAsZCETPZc0EP8obYGIebuynjJ-RoQk_Tg"
```

Replace with your own key:
```python
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
```

⚠️ **Security Warning**: Never share your API key publicly or commit it to GitHub!

**5️⃣ Launch the App**
```bash
streamlit run app.py
```

🎉 **Done!** The app opens automatically at `http://localhost:8501`

---

## 📖 User Guide

### 🚀 Getting Started

#### First-Time Setup (2 minutes)

1. **Open the Sidebar**
   - Click the `>` arrow in the top-left corner

2. **Complete Your Health Profile**
   
   Fill in these sections thoughtfully:

   **🎯 Health Goals**
   ```
   Examples:
   - Lose 20 pounds in 5 months
   - Build lean muscle mass
   - Maintain healthy weight
   - Improve energy levels
   - Better sleep quality
   ```

   **🏥 Medical Conditions**
   ```
   Examples:
   - Type 2 Diabetes
   - High blood pressure
   - High cholesterol
   - PCOS
   - None
   ```

   **💪 Fitness Routines**
   ```
   Examples:
   - 30-minute walk daily
   - Gym 4x per week (strength training)
   - Yoga 3x per week
   - Sedentary office job
   - Marathon training
   ```

   **🍽️ Food Preferences**
   ```
   Examples:
   - Vegetarian
   - Vegan
   - Pescatarian
   - Mediterranean diet
   - No restrictions
   ```

   **🚫 Dietary Restrictions**
   ```
   Examples:
   - Lactose intolerant
   - Gluten-free (Celiac disease)
   - Nut allergy
   - No pork (religious)
   - Low sodium diet
   ```

3. **Save Your Profile**
   - Click **"💾 Update Profile"**
   - Wait for the success message ✅

---

### 🍽️ Creating Your Meal Plan

**Step-by-Step:**

1. **Navigate to "🍽️ Meal Planning" Tab**

2. **Describe Your Needs** (optional but recommended)
   ```
   Great examples:
   - "Quick meals under 30 minutes"
   - "High protein for muscle building"
   - "Budget-friendly under $75/week"
   - "Meal prep for busy professionals"
   - "Family-friendly with kids"
   - "No cooking required"
   ```

3. **Select Duration**
   - 3 days: Perfect for trying new recipes
   - 7 days: Standard weekly planning
   - 14 days: Maximum variety and prep efficiency

4. **Generate Your Plan**
   - Click **"🎨 Generate Meal Plan"**
   - Wait 15-30 seconds for AI processing
   - Review your personalized plan

5. **What You'll Get:**
   - ✅ Complete daily menus with recipes
   - ✅ Nutritional breakdown per meal and per day
   - ✅ Detailed shopping list by category
   - ✅ Meal prep instructions and time estimates
   - ✅ Why each meal supports your goals
   - ✅ Alternative options for flexibility

6. **Save Your Plan**
   - Click **"📥 Download as Text"**
   - Save to your phone or print it out
   - Reference it while grocery shopping

7. **Need Something Different?**
   - Click **"🔄 Regenerate"** for a new plan
   - Modify your requirements and try again

**💡 Pro Tips:**
- Be specific about time constraints and cooking skills
- Mention budget limitations if relevant
- Specify if you need leftovers for lunch
- Update your profile before generating for best results

---

### 📸 Analyzing Your Food

**How to Get the Best Analysis:**

1. **Take a Great Photo**
   - ✅ Good lighting (natural light is best)
   - ✅ Show the entire meal
   - ✅ Photograph from above (bird's eye view)
   - ✅ Include a reference item (fork, plate edge)
   - ❌ Avoid blurry or dark images
   - ❌ Don't use heavy filters

2. **Upload Your Image**
   - Go to **"📸 Food Analysis"** tab
   - Click **"📸 Upload food image"**
   - Select JPG, JPEG, or PNG file (under 4MB)

3. **Choose Analysis Type**

   **🚀 Quick Analysis** (30 seconds)
   - Food identification
   - Calorie estimate
   - Basic macros (protein, carbs, fats)
   - One quick health tip
   - Best for: Daily tracking

   **🔬 Detailed Breakdown** (1 minute)
   - Complete ingredient list
   - Precise calorie count
   - Full macro and micronutrient profile
   - Portion size analysis
   - Preparation method evaluation
   - Best for: Learning about nutrition

   **🎯 Health Impact** (1 minute)
   - Everything in Detailed Breakdown
   - How it aligns with YOUR goals
   - Personalized recommendations
   - Suggested modifications
   - Better alternatives
   - Best for: Making better choices

4. **Review & Save**
   - Read your analysis carefully
   - Click **"💾 Save Analysis"** to download
   - Track your meals over time

**📝 Use Cases:**
- Restaurant meals: Know what you're really eating
- Home cooking: Verify your recipe's nutrition
- Meal prep: Ensure balanced nutrition
- Learning tool: Understand food better
- Accountability: Track your choices

---

### 💡 Getting Health Insights

**Ask the AI Nutritionist:**

1. **Go to "💡 Health Insights" Tab**

2. **Ask Your Question**
   
   **Great Question Examples:**
   ```
   General Questions:
   - "How much water should I drink daily?"
   - "What are the best protein sources for vegetarians?"
   - "How can I reduce sugar cravings?"
   - "What foods help with better sleep?"
   
   Goal-Specific:
   - "How can I boost my energy naturally?"
   - "What should I eat before a workout?"
   - "Best foods for muscle recovery?"
   - "How to increase fiber intake?"
   
   Medical-Related:
   - "What foods help lower blood pressure?"
   - "Best diet for managing diabetes?"
   - "How to eat for better gut health?"
   - "Foods that reduce inflammation?"
   ```

3. **Toggle "Use my profile"**
   - ✅ **ON**: Get personalized advice for YOUR situation
   - ⬜ **OFF**: Get general health information

4. **Get Your Answer**
   - Click **"🧠 Get Expert Insights"**
   - Wait 10-20 seconds for response
   - Read comprehensive, science-backed advice

5. **What You'll Receive:**
   - 📚 Clear scientific explanation
   - 🎯 Personalized recommendations (if profile mode on)
   - ✅ Actionable steps you can start today
   - ⚠️ Relevant precautions
   - 🥗 Specific food and supplement suggestions

6. **Save & Track**
   - Download insights with **"💾 Save Insights"**
   - View recent questions in the history below
   - Build your personal health knowledge library

**💡 Pro Tips:**
- Ask follow-up questions for deeper understanding
- Be specific about your situation
- Use profile mode for personalized advice
- Save important insights for reference
- Cross-check advice with your healthcare provider

---

### 📊 Profile & Statistics

**Track Your Journey:**

1. **View Your Profile**
   - See all your health information in JSON format
   - Verify everything is up-to-date
   - Review your goals and preferences

2. **Check Activity Metrics**
   - **Questions Asked**: Total health insights requested
   - **Meal Plans Generated**: How many plans you've created
   - Track your engagement with the app

3. **Manage History**
   - Click **"🗑️ Clear Chat History"** to reset
   - Start fresh when beginning a new health phase
   - Keep recent questions for active reference

4. **Pro Tips Section**
   - Review best practices
   - Learn how to get better results
   - Discover features you might have missed

---

## ⚙️ Customization & Advanced Settings

### Changing the AI Model

In the code, find:
```python
model = genai.GenerativeModel('gemini-2.5-flash')
```

**Available Models:**

| Model | Speed | Detail | Best For | Token Limit |
|-------|-------|--------|----------|-------------|
| `gemini-2.5-flash` | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | Daily use (recommended) | 1M |
| `gemini-2.5-pro` | ⚡⚡ Medium | ⭐⭐⭐⭐⭐ Excellent | Complex analysis | 2M |
| `gemini-1.5-flash` | ⚡⚡⚡ Fast | ⭐⭐ Basic | Quick answers | 1M |
| `gemini-1.5-pro` | ⚡ Slower | ⭐⭐⭐⭐ Very Good | Research | 2M |

### Adjusting Page Layout

```python
st.set_page_config(
    page_title="AI Health Companion",  # Browser tab title
    layout="wide",  # Change to "centered" for narrower view
    page_icon="🏥"  # Change emoji icon
)
```

### Adding More Meal Plan Durations

Find and modify:
```python
meal_duration = st.selectbox(
    "Meal plan duration:",
    ["3 days", "7 days", "14 days", "21 days", "30 days"],  # Add more options
    index=1
)
```

### Customizing Default Profile

Edit the default values:
```python
st.session_state.health_profile = {
    'goals': 'Your default goals here',
    'conditions': 'Your conditions',
    'routines': 'Your routines',
    'preferences': 'Your preferences',
    'restrictions': 'Your restrictions'
}
```

---

## 🐛 Troubleshooting Guide

### ❌ "Error generating response"

**Possible Causes & Solutions:**

**1. Invalid API Key**
```
Problem: API key is incorrect or expired
Solution:
- Check for typos in your API key
- Ensure no extra spaces before/after key
- Regenerate key at https://aistudio.google.com/apikey
- Verify key is active in Google AI Studio
```

**2. API Quota Exceeded**
```
Problem: You've hit the free tier limit
Free Tier Limits:
- 60 requests per minute
- 1,500 requests per day
- 1 million tokens per month

Solution:
- Wait for the quota to reset (resets daily)
- Monitor usage at Google AI Studio
- Upgrade to paid tier for higher limits
- Space out your requests
```

**3. Network/Connection Issues**
```
Problem: Can't reach Google's servers
Solution:
- Check your internet connection
- Try accessing google.com
- Disable VPN temporarily
- Check firewall settings
- Try again in a few minutes
```

### 🖼️ Image Upload Problems

**Issue: Image won't upload**
```
Solutions:
✅ Verify format is JPG, JPEG, or PNG
✅ Check file size (must be under 4MB)
✅ Compress large images using tinypng.com
✅ Try a different image
✅ Clear browser cache (Ctrl+Shift+Del)
✅ Use a different browser
```

**Issue: "Error processing image"**
```
Solutions:
✅ Ensure image isn't corrupted
✅ Try converting to different format
✅ Take a new photo
✅ Restart the app
```

### 🔄 App Not Loading or Stuck

**Quick Fixes:**

```bash
# Stop the app (Ctrl+C in terminal)

# Clear Streamlit cache
streamlit cache clear

# Try a different port
streamlit run app.py --server.port 8502

# Restart your computer
# Then try again
```

**Advanced Fixes:**

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or force reinstall
pip install --force-reinstall -r requirements.txt

# Check for conflicting Python versions
python --version
```

### 🚫 "Module not found" Error

```bash
# Install missing package individually
pip install streamlit
pip install google-generativeai
pip install python-dotenv
pip install Pillow

# Or reinstall everything
pip install -r requirements.txt --force-reinstall
```

### 💾 Profile Not Saving

**Checklist:**
- ✅ Did you click "💾 Update Profile" button?
- ✅ Did you wait for the "✅ Profile updated" message?
- ✅ Check the sidebar to verify changes
- ✅ Try refreshing the page (F5)
- ✅ Clear browser cache and try again

### ⚡ Slow Response Times

**Optimization Tips:**
- Close other browser tabs
- Use Quick Analysis instead of Detailed
- Reduce image file sizes
- Check your internet speed
- Try during off-peak hours
- Consider upgrading to Gemini Pro model

### 🔴 Port Already in Use

```bash
# Error: Address already in use
# Solution: Kill the process or use different port

# Find and kill the process (Windows)
netstat -ano | findstr :8501
taskkill /PID <process_id> /F

# Find and kill the process (Mac/Linux)
lsof -ti:8501 | xargs kill -9

# Or use a different port
streamlit run app.py --server.port 8502
```

---

## 🔐 Security & Privacy

### 🔑 API Key Security Best Practices

**❌ NEVER DO THIS:**
```python
# DON'T hardcode API keys in production
GOOGLE_API_KEY = "AIzaSyAsZCETPZc0EP8obYGIebuynjJ-RoQk_Tg"

# DON'T commit keys to GitHub
git add app.py  # Contains your API key

# DON'T share keys in screenshots or videos
# DON'T paste keys in public forums
```

**✅ DO THIS INSTEAD:**

**Method 1: Environment Variables (.env file)**
```bash
# Create .env file
echo "GOOGLE_API_KEY=your_key_here" > .env

# Update code to use it
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Add .env to .gitignore
echo ".env" >> .gitignore
```

**Method 2: Streamlit Secrets (for deployment)**
```bash
# Create .streamlit/secrets.toml
mkdir .streamlit
echo 'GOOGLE_API_KEY = "your_key_here"' > .streamlit/secrets.toml

# Access in code
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
```

### 📁 .gitignore Setup

Create a `.gitignore` file:
```gitignore
# API Keys and Secrets
.env
.env.local
.env.production
.streamlit/secrets.toml

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Streamlit
.streamlit/

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# OS
Thumbs.db
.DS_Store

# User data
user_data/
uploads/
```

### 🔒 Data Privacy

**What Gets Stored:**
- ✅ Your health profile (session only)
- ✅ Chat history (session only)
- ✅ Generated meal plans (session only)

**What Doesn't Get Stored:**
- ❌ No data saved to disk
- ❌ No database connections
- ❌ No user accounts or passwords

**Important Notes:**
- All data clears when you close the browser
- Food images sent to Google's Gemini API
- Review [Google's Privacy Policy](https://policies.google.com/privacy)
- For sensitive health data, consult professionals

### 🛡️ API Key Rotation

**Best Practice: Rotate keys regularly**

```bash
# Every 3-6 months:
1. Generate new API key at aistudio.google.com
2. Update your .env file
3. Delete old key from Google AI Studio
4. Restart the app
```

---

## 📊 API Usage & Optimization

### Free Tier Limits (Google Gemini API)

| Limit Type | Free Tier | Pro Tier |
|------------|-----------|----------|
| Requests/Minute | 60 | 1,000 |
| Requests/Day | 1,500 | 1,000,000 |
| Tokens/Month | 1,000,000 | Unlimited |
| Rate Limit | Yes | Higher |

### Staying Within Free Tier

**Smart Usage Strategies:**

1. **Batch Similar Requests**
   - Generate weekly plans instead of daily
   - Ask comprehensive questions
   - Download and reuse insights

2. **Use Appropriate Analysis Depth**
   - Quick Analysis for daily tracking
   - Detailed only when needed
   - Save previous analyses

3. **Optimize Prompts**
   - Be specific and concise
   - Avoid redundant questions
   - Reuse similar meal plans

4. **Monitor Your Usage**
   - Check [Google AI Studio](https://aistudio.google.com/)
   - Track requests per day
   - Set up usage alerts

5. **Time Your Requests**
   - Spread throughout the day
   - Avoid rapid-fire requests
   - Plan ahead for busy days

### Token Usage Tips

**What Counts as Tokens:**
- Input text (your prompts)
- Output text (AI responses)
- Image data (food photos)

**How to Reduce Token Usage:**
```python
# Keep prompts concise
# Use shorter meal plan durations
# Compress images before uploading
# Download plans instead of regenerating
```

---

## ⚠️ Important Disclaimers

### 🏥 Medical & Health Information

**Please Read Carefully:**

This application provides **general health and nutritional information** for educational purposes only. It is **NOT**:

- ❌ A substitute for professional medical advice
- ❌ A diagnostic tool for medical conditions
- ❌ Treatment recommendations from licensed professionals
- ❌ Personalized medical advice from a doctor
- ❌ Approved by any medical or regulatory authority

**You Should Always:**
- ✅ Consult with your doctor before starting any diet
- ✅ Discuss medical conditions with healthcare providers
- ✅ Get professional advice for serious health concerns
- ✅ Verify AI suggestions with qualified nutritionists
- ✅ Use your own judgment and common sense

### 🥗 Nutritional Analysis Accuracy

**Important Notes:**

- Calorie counts are **estimates only**
- Portion sizes may vary significantly
- Individual nutritional needs differ
- Food preparation affects nutrition
- AI analysis may contain errors

**For Precise Nutrition:**
- Consult a registered dietitian
- Use calibrated food scales
- Track with verified nutrition apps
- Get lab tests for deficiencies

### 🤖 AI Limitations

**This AI May:**
- Occasionally provide incorrect information
- Miss nuances in complex health situations
- Not have the latest research
- Misinterpret food images
- Provide outdated recommendations

**Always:**
- Cross-reference important advice
- Use critical thinking
- Verify with reliable sources
- Trust your healthcare providers

### 🚨 When to Seek Professional Help

**Consult a doctor immediately if you:**
- Have severe or persistent symptoms
- Are starting a new medication
- Have chronic health conditions
- Are pregnant or breastfeeding
- Experience unusual reactions
- Need medical diagnosis

---

##  Pro Tips & Best Practices

###  For Maximum Meal Planning Success

**Before Generating:**
-  Update your profile completely
-  Be honest about cooking skills
-  Specify time and budget constraints
-  Mention family size if relevant
-  Note any equipment limitations

**While Using:**
-  Generate multiple variations
-  Save your favorite plans
-  Adjust portions to your needs
-  Swap meals between days
-  Print and keep visible

**After Generating:**
-  Shop once for the week
-  Prep ingredients in batches
-  Use containers for portions
-  Freeze extra servings
-  Track what works for you

### 📸 For Accurate Food Analysis

**Photo Quality Matters:**
-  Natural daylight works best
-  Shoot from directly above
-  Include entire plate in frame
-  Add fork/spoon for scale
-  Avoid shadows and glare
-  Keep background simple

**What to Analyze:**
-  Restaurant meals (learn portions)
-  Home cooking (verify recipes)
-  Meal prep (ensure balance)
-  Snacks (track hidden calories)
-  New foods (learn nutrition)

###  For Better Health Insights

**Asking Questions:**
-  Be specific about your situation
-  Include relevant context
-  Ask follow-up questions
-  Request practical examples
-  Clarify confusing points

**Using Answers:**
-  Implement one tip at a time
-  Track what works for you
-  Share with your support system
-  Revisit saved insights regularly
-  Update practices as you learn

### Tracking Your Progress

**Create a System:**
1. Download all meal plans
2. Save food analyses weekly
3. Keep health insights organized
4. Review progress monthly
5. Adjust profile as you improve

**Document Your Journey:**
- Take progress photos
- Track energy levels
- Note how you feel
- Measure real outcomes
- Celebrate small wins

---

##  Version History & Roadmap

### Current Version: 1.0.0

** Features:**
-  Personalized meal planning (3/7/14 days)
-  AI-powered food image analysis
-  Health Q&A with chat history
-  Comprehensive health profile system
-  Activity tracking dashboard
-  Download functionality for all content

** Known Issues:**
- None currently reported

###  Planned Features (v1.1.0+)

**Coming Soon:**
-  Daily meal reminders via email
-  Progress tracking with charts
-  Searchable recipe database
-  Smart grocery list generator
-  Cloud sync for profile data
-  Mobile-optimized interface

**Future Roadmap:**
-  Multi-user/family support
-  Integration with fitness trackers
-  Video meal prep tutorials
-  International cuisine support
-  Calendar integration
-  Advanced analytics dashboard

**Want a Feature?**
- Open a GitHub issue
- Describe your use case
- Vote on existing requests

---

##  Contributing

We welcome contributions! Here's how you can help:

###  Report Bugs

1. Check if bug already reported
2. Use GitHub Issues
3. Include:
   - Error message (full text)
   - Steps to reproduce
   - Screenshots if applicable
   - Your Python version
   - Your OS (Windows/Mac/Linux)

###  Suggest Features

1. Check existing feature requests
2. Open a new issue
3. Describe:
   - What you want to achieve
   - Why it would be useful
   - How it might work
   - Any examples from other apps

###  Submit Code

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
6. Describe your changes clearly

###  Improve Documentation

- Fix typos or unclear instructions
- Add more examples
- Translate to other languages
- Create video tutorials
- Write blog posts

---

##  Technical Details

### System Requirements

**Minimum:**
- Python 3.8+
- 2GB RAM
- Internet connection
- Modern web browser

**Recommended:**
- Python 3.10+
- 4GB+ RAM
- Fast internet (for image uploads)
- Chrome/Firefox latest version

### Dependencies

```
streamlit==1.31.0       # Web framework
google-generativeai==0.3.2  # Gemini AI SDK
python-dotenv==1.0.0    # Environment variables
Pillow==10.2.0          # Image processing
```

### File Structure

```
ai-health-companion/
│
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # This file
├── .env                  # API keys (create this)
├── .gitignore           # Git ignore file
│
└── .streamlit/
    └── secrets.toml      # Streamlit secrets (optional)
```

### Performance Notes

- First request may be slow (model loading)
- Subsequent requests are cached
- Image analysis takes 10-30 seconds
- Meal plans take 15-45 seconds
- Health insights take 10-20 seconds

---

##  Support & Community

###  Get Help

**For App Issues:**
1. Check Troubleshooting section
2. Review error messages carefully
3. Try basic fixes first
4. Search GitHub Issues
5. Create new issue if needed

**For API Issues:**
- [Google AI Documentation](https://ai.google.dev/docs)
- [API Status Page](https://status.cloud.google.com/)
- [Pricing & Quotas](https://ai.google.dev/pricing)
- [Community Forum](https://discuss.ai.google.dev/)

**For Streamlit Issues:**
- [Streamlit Docs](https://docs.streamlit.io)
- [Community Forum](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

###  Community

-  [Discord Server](#) (coming soon)
-  [Twitter Updates](#) (coming soon)
-  [YouTube Tutorials](#) (coming soon)
-  [Reddit Community](#) (coming soon)

---

##  Acknowledgments

**Special Thanks To:**

- **Google Gemini Team** - For the incredible AI models
- **Streamlit Team** - For the amazing web framework
- **Python Community** - For excellent libraries
- **Early Testers** - For valuable feedback
- **You** - For using this app!

**Built With:**
- [Google Gemini API](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)
- [Pillow](https://python-pillow.org/)

---

## 📜 License

This project is available for personal and educational use.

**You Can:**
- ✅ Use for personal health tracking
- ✅ Modify for your own needs
- ✅ Learn from the code
- ✅ Share with friends

**You Cannot:**
- ❌ Sell this application
- ❌ Claim as your own work
- ❌ Remove attribution

**Please Comply With:**
- [Google Gemini API Terms](https://ai.google.dev/terms)
- [Streamlit Terms of Use](https://streamlit.io/terms-of-use)

---

## 📫 Contact & Links

**Project Information:**
- 🌐 Website: [Your Website]
- 📧 Email: [Your Email]
- 🐙 GitHub: [Your GitHub Profile]
- 💼 LinkedIn: [Your LinkedIn]

**Report Issues:**
- 🐛 [GitHub Issues Page]
- 📬 Direct email for urgent matters

---

<div align="center">

##  Star This Project!

If you find this helpful, please give it a star on GitHub!

**Made with  by [Your Name]**

*Powered by Google Gemini 2.5 Flash & Streamlit*

---

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)
![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.5-4285F4?style=for-the-badge&logo=google)
![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)

**Version 1.0.0** | Last Updated: January 2025

</div>

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