# Quick Start Guide - AI Layout Planner

## ⚡ Quick Setup (2 minutes)

### For Windows Users:
1. Open Command Prompt and navigate to the project folder:
   ```
   cd c:\visual studio\project1
   ```

2. Run the startup script:
   ```
   run.bat
   ```

3. Open your browser and go to: **http://localhost:5000**

### For Mac/Linux Users:
1. Open Terminal and navigate to the project folder:
   ```
   cd /path/to/project1
   ```

2. Make the script executable and run it:
   ```
   chmod +x run.sh
   ./run.sh
   ```

3. Open your browser and go to: **http://localhost:5000**

### Manual Setup (if scripts don't work):
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## 📖 Website Pages

### 1. **Home** (http://localhost:5000/)
- Landing page with features overview
- Quick links to all sections
- Feature highlights

### 2. **About** (http://localhost:5000/about)
- Detailed project information
- Technology stack details
- How the AI algorithm works
- Why use this tool

### 3. **Planner** (http://localhost:5000/planner) ⭐ MAIN FEATURE
**Input Form:**
- Population (e.g., 100,000)
- Temperature (e.g., 25°C)
- Weather (Sunny, Rainy, Cloudy, Snow, Moderate, Tropical)
- Road Infrastructure (Basic, Normal, Advanced, Modern)

**Outputs:**
- Grid-based city layout visualization
- Population density classification
- Road width recommendations
- Amenity suggestions
- Development recommendations

### 4. **Contact** (http://localhost:5000/contact)
- Contact form
- Business information
- FAQ section

## 🎯 How to Use the AI Planner

### Step 1: Input Your City Parameters
Fill in the form on the Planner page:
- **Population**: Enter your city's population
- **Temperature**: Average temperature in Celsius
- **Weather**: Select the climate type
- **Roads**: Rate current road infrastructure

### Step 2: Generate Layout
Click "Generate Layout" button and wait for AI analysis (5-10 seconds)

### Step 3: Analyze Results
Review the generated layout which includes:
- **Visual Grid**: Color-coded zones (Residential, Commercial, Parks, Industrial)
- **Density Analysis**: How crowded your city will be
- **Road Design**: Recommended road widths (1-4 levels)
- **Amenities**: Suggested parks, hospitals, transit hubs, etc.
- **Recommendations**: Strategic development advice

### Step 4: Extract Insights
Use the recommendations for:
- Urban planning decisions
- Infrastructure investment planning
- Amenity distribution
- Traffic management strategies

## 📊 Understanding the Layout Grid

The visualization uses a 10x10 grid with color coding:

| Color | Zone Type | Purpose |
|-------|-----------|---------|
| Gray | Roads | Transportation network |
| Yellow | Residential | Housing areas |
| Red | Commercial | Shopping, offices, businesses |
| Green | Parks & Green Space | Recreation, environment |
| Dark Gray | Industrial | Manufacturing, logistics |

## 💡 Example Scenario

**Input:**
- Population: 250,000
- Temperature: 28°C
- Weather: Tropical
- Roads: Normal

**Expected Output:**
- Density: High
- Road Width: Level 3/4 (wider roads needed)
- Amenities: Parks, Shopping malls, Water fountains, Cooling centers, Public transit
- Recommendations: Implement multi-level parking, develop rapid transit system, maximize green spaces

## 🔧 Troubleshooting

**Port 5000 already in use?**
- Edit `backend/app.py`, line: `app.run(port=5001)`

**Module import errors?**
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt` again

**Layout not generating?**
- Check browser console (F12) for errors
- All form fields must be filled
- Population should be between 1,000 and 10,000,000+

**Page not loading?**
- Make sure Flask server is running
- Try clearing browser cache (Ctrl+Shift+Delete)
- Use incognito/private mode

## 📧 Contact Information

- Email: info@ailayoutplanner.com
- Phone: +1 (555) 123-4567
- Hours: Monday-Friday, 9 AM - 6 PM

## 🚀 Next Steps

1. Try the planner with different city scenarios
2. Compare layouts for different populations
3. Explore how climate affects recommendations
4. Check contact page for more information
5. Share feedback or questions via contact form

---

**You're all set! Start creating smarter city layouts! 🏗️✨**
