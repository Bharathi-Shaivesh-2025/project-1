# AI Layout Planner 🏗️

A sophisticated web application that uses artificial intelligence to generate optimized city layouts based on population, climate, and infrastructure parameters.

## Project Overview

**AI Layout Planner** is a full-stack web application designed for urban planners, architects, and city developers. It leverages AI and statistical analysis to create data-driven city layouts that consider:

- **Population Density** - Affects road width and infrastructure allocation
- **Climate Conditions** - Temperature influences amenity recommendations
- **Weather Patterns** - Impacts infrastructure needs (drainage, cooling, etc.)
- **Road Infrastructure** - Current state to inform expansion planning

## Features

✨ **Key Capabilities:**
- 📊 Real-time population density analysis
- 🌡️ Climate-aware amenity recommendations
- 🛣️ Smart road planning with adaptive widths
- 🌳 Optimal park and green space allocation
- 📈 Beautiful grid-based layout visualization
- 💡 Personalized development recommendations
- 📱 Responsive, modern UI design

## Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern flex/grid layouts with animations
- **JavaScript** - Interactive UI and API communication

### Backend
- **Python 3.8+** - Core programming language
- **Flask 2.3.2** - Web framework
- **Flask-CORS 4.0.0** - Cross-Origin Resource Sharing support
- **NumPy 1.24.3** - Numerical computing
- **Matplotlib 3.7.1** - Data visualization
- **SciPy 1.11.0** - Scientific computing
- **Pandas 2.0.3** - Data analysis

## Project Structure

```
project1/
├── backend/
│   ├── app.py                 # Flask application & routes
│   ├── layout_planner.py      # AI layout planning logic
│   ├── requirements.txt       # Python dependencies
│   ├── templates/
│   │   ├── index.html         # Homepage
│   │   ├── about.html         # About page
│   │   ├── planner.html       # Main planner interface
│   │   └── contact.html       # Contact page
│   └── static/
│       ├── style.css          # Main stylesheet
│       ├── script.js          # General JavaScript
│       ├── planner.js         # Planner-specific logic
│       └── contact.js         # Contact form logic
└── frontend/                  # (Optional) Standalone frontend files
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone or Download the Project
```bash
cd c:\visual studio\project1
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start at: **http://localhost:5000**

## Usage Guide

### 1. **Homepage** (/)
- Overview of features
- Quick introduction to the AI Layout Planner
- Navigation to other sections

### 2. **About Page** (/about)
- Detailed information about the project
- Technology stack explanation
- How the AI algorithm works
- Benefits and use cases

### 3. **AI Planner** (/planner) - Main Feature
Input parameters:
- **Population**: City population (1,000 to 10,000,000+)
- **Temperature**: Current/average temperature in °C
- **Weather**: Select from Sunny, Rainy, Cloudy, Snow, Moderate, Tropical
- **Road Infrastructure**: Current state (Basic, Normal, Advanced, Modern)

Output includes:
- **Grid-based layout visualization** with color-coded zones
- **Population density classification** (Low, Medium, High, Very High)
- **Road recommendations** (width levels 1-4)
- **Amenity suggestions** (parks, transit hubs, hospitals, etc.)
- **Development recommendations** specific to your city

### 4. **Contact Page** (/contact)
- Contact form for inquiries
- Direct contact information
- FAQ section with common questions

## AI Algorithm Explanation

### Population Density Classification
```
Low:       < 10,000 people      → Narrow roads, rural focus
Medium:    10,000 - 50,000      → Balanced infrastructure
High:      50,000 - 200,000     → Wide roads, urban density
Very High: > 200,000            → Highways, metropolitan
```

### Road Width Determination
- **Level 1**: Narrow roads (1-2 lane) for low-density areas
- **Level 2**: Medium roads (2-3 lanes) for balanced cities
- **Level 3**: Wide roads (3-4 lanes) for high-density areas
- **Level 4**: Highways (4+ lanes) for metropolitan areas

### Zone Allocation
- **Residential Zones**: Housing and family areas (Yellow)
- **Commercial Zones**: Shopping, offices, businesses (Red)
- **Parks & Green Spaces**: Recreation and environment (Green)
- **Industrial Zones**: Manufacturing, logistics (Dark Gray)
- **Roads**: Transit networks (Gray)

### Climate-Based Amenities
- **Hot Climate** (>30°C): Shopping malls, water fountains, cooling centers
- **Cold Climate** (<10°C): Community centers, recreation halls
- **Rainy Areas**: Underground drainage, covered walkways
- **Snow Areas**: Snow removal infrastructure
- **High Density**: Public transit, hospitals, schools, markets

## API Endpoints

### POST /api/generate-layout
Generate a complete city layout and analysis.

**Request:**
```json
{
    "population": 100000,
    "temperature": 25,
    "weather": "Moderate",
    "roads": "Normal"
}
```

**Response:**
```json
{
    "success": true,
    "layout_image": "data:image/png;base64,...",
    "report": {
        "population": "100,000",
        "density": "Medium",
        "temperature": "25°C",
        "weather": "Moderate",
        "road_width": "Width Level: 2/4",
        "road_description": "...",
        "amenities": ["Parks", "..."],
        "recommendations": ["..."],
        "timestamp": "2026-02-26 10:30:00"
    }
}
```

### POST /api/get-recommendations
Get quick recommendations without full layout generation.

### POST /api/contact
Submit contact form inquiries.

## Data Visualization

The planner generates a **10x10 grid** representing the city layout with:
- Color-coded zones for different land uses
- Grid overlay for easy reference
- Total area representation
- Automatic scaling based on population

## Advanced Features

### Statistical Analysis
- Uses NumPy for numerical calculations
- Matplotlib for grid visualization
- SciPy for advanced statistical modeling

### Smart Recommendations
The AI provides context-aware suggestions based on:
- Population growth patterns
- Climate adaptation needs
- Infrastructure efficiency
- Sustainable development principles

## Customization

### Modify Grid Size
Edit `layout_planner.py`, line ~32:
```python
self.grid_size = 10  # Change to desired size
```

### Add Custom Amenities
Modify `_suggest_amenities()` method in `layout_planner.py`

### Adjust Color Scheme
Edit `style.css` CSS variables:
```css
:root {
    --primary-color: #4A90E2;
    --secondary-color: #7B68EE;
    --accent-color: #F39C12;
}
```

## Performance Considerations

- Layout generation: 2-10 seconds per request
- API response time: <500ms
- Static file serving: Optimized with Flask
- Matplotlib rendering: Cached in base64 format

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(port=5001)
```

### Module Not Found
Ensure all requirements are installed:
```bash
pip install -r requirements.txt
```

### Display Issues
Clear browser cache and try again, or use incognito mode.

## Future Enhancements

- User authentication and saved projects
- Export layouts to CAD/PDF formats
- Multi-city comparison tool
- Historical data analysis
- Real-time traffic simulation
- 3D visualization support
- Database integration for data persistence
- Mobile app version
- API for third-party integrations

## License

This project is created for educational and professional urban planning purposes.

## Support & Contact

For questions or support:
- 📧 Email: info@ailayoutplanner.com
- 🌐 Website: www.ailayoutplanner.com
- 💼 LinkedIn: [AI Layout Planner]

---

**Build smarter cities with AI-powered urban planning! 🏙️✨**
