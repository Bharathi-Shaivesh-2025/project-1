import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec
import io
import base64
from datetime import datetime

class AILayoutPlanner:
    """
    AI-powered city layout planner that generates layouts based on:
    - Population density
    - Temperature
    - Weather conditions
    - Road infrastructure
    """
    
    def __init__(self, population, temperature, weather, roads):
        self.population = population
        self.temperature = temperature
        self.weather = weather
        self.roads = roads
        self.grid_size = 1000
        self.layout = np.zeros((self.grid_size, self.grid_size))
        
    def calculate_density(self):
        """Calculate population density category"""
        if self.population < 10000:
            return "Low"
        elif self.population < 50000:
            return "Medium"
        elif self.population < 200000:
            return "High"
        else:
            return "Very High"
    
    def determine_road_width(self):
        """Determine road width based on population density"""
        density = self.calculate_density()
        
        if density == "Low":
            return 1  # Narrow roads
        elif density == "Medium":
            return 2
        elif density == "High":
            return 3  # Wider roads
        else:
            return 4  # Very wide roads
    
    def suggest_amenities(self):
        """Suggest amenities based on weather and population"""
        amenities = []
        
        # Always include parks
        amenities.append("Parks & Green Spaces")
        
        if int(self.temperature) > 30:
            amenities.extend(["Shopping Malls (indoor)", "Water Fountains", "Cooling Centers"])
        elif int(self.temperature) < 10:
            amenities.extend(["Community Centers", "Recreation Halls"])
        else:
            amenities.extend(["Outdoor Recreation Areas", "Playgrounds"])
        
        # Weather-based suggestions
        if "Rain" in self.weather or "Rainy" in self.weather:
            amenities.append("Underground Drainage System")
            amenities.append("Covered Walkways")
        
        if "Snow" in self.weather:
            amenities.append("Snow Removal Infrastructure")
        
        # Population-based amenities
        density = self.calculate_density()
        if density in ["High", "Very High"]:
            amenities.extend(["Public Transit Hubs", "Hospitals", "Schools", "Markets"])
        
        return list(set(amenities))
    
    def generate_layout_grid(self):
        """Generate a grid-based city layout"""
        layout = np.zeros((self.grid_size, self.grid_size))
        road_width = self.determine_road_width()
        
        # Create main roads (highways) - scaled for 1000x1000 grid
        layout[::30, :] = 1  # Horizontal main roads
        layout[:, ::30] = 1  # Vertical main roads
        
        # Create secondary roads based on population
        if self.calculate_density() in ["High", "Very High"]:
            layout[10::30, :] = 1  # Additional horizontal roads
            layout[:, 10::30] = 1  # Additional vertical roads
        
        # Allocate zones (scaled for 1000x1000 grid)
        # Residential zones
        layout[100:200, 100:200] = 2
        layout[400:600, 400:600] = 2
        layout[700:900, 700:900] = 2
        
        # Commercial zones
        layout[400:600, 100:200] = 3
        layout[100:200, 700:900] = 3
        
        # Parks and green spaces
        layout[400:600, 700:900] = 4
        layout[700:900, 100:300] = 4
        
        # Industrial zones (for high density only)
        if self.calculate_density() in ["High", "Very High"]:
            layout[700:900, 400:600] = 5
        
        return layout
    
    def create_visualization(self):
        """Create grid visualization of the layout"""
        layout = self.generate_layout_grid()
        
        fig, ax = plt.subplots(figsize=(16, 16))
        
        # Color map for different zones
        colors = {
            0: '#E8E8E8',  # Empty/Parks area
            1: '#808080',  # Roads (gray)
            2: '#FFD700',  # Residential (yellow)
            3: '#FF6B6B',  # Commercial (red)
            4: '#90EE90',  # Parks (green)
            5: '#A9A9A9'   # Industrial (dark gray)
        }
        
        # Create colored grid
        colored_layout = np.zeros((self.grid_size, self.grid_size, 3))
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = colors.get(layout[i, j], '#FFFFFF')
                colored_layout[i, j] = self._hex_to_rgb(color)
        
        ax.imshow(colored_layout)
        
        # Add grid (every 50 cells for 1000x1000 to avoid overcrowding)
        grid_interval = 50
        for i in range(0, self.grid_size + 1, grid_interval):
            ax.axhline(i - 0.5, color='black', linewidth=0.3, alpha=0.5)
            ax.axvline(i - 0.5, color='black', linewidth=0.3, alpha=0.5)
        
        ax.set_xticks(range(0, self.grid_size, grid_interval))
        ax.set_yticks(range(0, self.grid_size, grid_interval))
        ax.set_title(f"AI-Generated City Layout\nPopulation: {self.population:,} | Density: {self.calculate_density()}", 
                     fontsize=14, fontweight='bold')
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor=colors[1], label='Roads'),
            patches.Patch(facecolor=colors[2], label='Residential'),
            patches.Patch(facecolor=colors[3], label='Commercial'),
            patches.Patch(facecolor=colors[4], label='Parks & Green Space'),
            patches.Patch(facecolor=colors[5], label='Industrial')
        ]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
        
        plt.tight_layout()
        
        # Convert to base64 for web display
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return image_base64
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB normalized to 0-1"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))
    
    def generate_report(self):
        """Generate a detailed analysis report"""
        density = self.calculate_density()
        road_width = self.determine_road_width()
        amenities = self.suggest_amenities()
        
        report = {
            "population": f"{self.population:,}",
            "density": density,
            "temperature": f"{self.temperature}°C",
            "weather": self.weather,
            "road_width": f"Width Level: {road_width}/4",
            "road_description": self._get_road_description(road_width, density),
            "amenities": amenities,
            "recommendations": self._get_recommendations(density),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return report
    
    def _get_road_description(self, width, density):
        """Get description for road width"""
        descriptions = {
            1: "Narrow roads suitable for low-traffic areas. Good for pedestrian-friendly communities.",
            2: "Medium-width roads for local traffic. Balanced between vehicle and pedestrian needs.",
            3: "Wider roads with multiple lanes. Designed for higher traffic volume and faster commute.",
            4: "Very wide roads (highways/motorways). Essential for metropolitan areas with heavy traffic."
        }
        return descriptions.get(width, "Standard roads")
    
    def _get_recommendations(self, density):
        """Get recommendations based on density"""
        recommendations = []
        
        if density == "Low":
            recommendations.append("Plan for agricultural areas and conservation zones")
            recommendations.append("Focus on community centers and local markets")
        elif density == "Medium":
            recommendations.append("Balance between commercial and residential development")
            recommendations.append("Invest in local public transportation")
        elif density == "High":
            recommendations.append("Implement multi-level parking structures")
            recommendations.append("Develop rapid transit systems (metro/buses)")
            recommendations.append("Maximize vertical development (high-rises)")
        else:
            recommendations.append("Implement advanced smart city infrastructure")
            recommendations.append("Develop comprehensive public transportation network")
            recommendations.append("Plan mixed-use developments")
        
        return recommendations
