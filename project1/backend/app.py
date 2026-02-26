from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from layout_planner import AILayoutPlanner
import json

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# ============= ROUTES =============

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/planner')
def planner():
    """AI Layout Planner page"""
    return render_template('planner.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

# ============= API ENDPOINTS =============

@app.route('/api/generate-layout', methods=['POST'])
def generate_layout():
    """
    API endpoint to generate city layout
    
    Expected JSON:
    {
        "population": int,
        "temperature": float,
        "weather": str,
        "roads": str
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ['population', 'temperature', 'weather', 'roads']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create planner instance
        planner = AILayoutPlanner(
            population=int(data['population']),
            temperature=float(data['temperature']),
            weather=data['weather'],
            roads=data['roads']
        )
        
        # Generate layout and report
        layout_image = planner.create_visualization()
        report = planner.generate_report()
        
        return jsonify({
            'success': True,
            'layout_image': f'data:image/png;base64,{layout_image}',
            'report': report
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get-recommendations', methods=['POST'])
def get_recommendations():
    """Get quick recommendations based on inputs"""
    try:
        data = request.get_json()
        
        planner = AILayoutPlanner(
            population=int(data.get('population', 10000)),
            temperature=float(data.get('temperature', 20)),
            weather=data.get('weather', 'Moderate'),
            roads=data.get('roads', 'Normal')
        )
        
        return jsonify({
            'density': planner.calculate_density(),
            'amenities': planner.suggest_amenities(),
            'road_width': planner.determine_road_width()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        # Validate
        required = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # In production, save to database or send email
        print(f"\nContact Form Submission:")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Subject: {data['subject']}")
        print(f"Message: {data['message']}\n")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
