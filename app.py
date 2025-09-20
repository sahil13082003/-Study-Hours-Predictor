from flask import Flask, render_template, request, flash, jsonify
import pickle
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('n', 'n')


# Global variable for model
model_package = None

def load_model():
    """Load the trained model"""
    global model_package
    model_path = 'models/study_model.pkl'
    
    try:
        if not os.path.exists(model_path):
            logger.error(f"Model file not found at {model_path}")
            return False
        
        with open(model_path, 'rb') as file:
            model_package = pickle.load(file)
        
        logger.info("Model loaded successfully!")
        return True
    
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return False

def validate_input(data):
    """Validate user input"""
    try:
        study_hours = float(data.get('study_hours', 0))
        previous_score = float(data.get('previous_score', 0))
        sleep_hours = float(data.get('sleep_hours', 0))
        attendance = float(data.get('attendance', 0))
        
        # Validation rules
        if not (0 <= study_hours <= 12):
            return False, "Study hours must be between 0 and 12"
        
        if not (0 <= previous_score <= 100):
            return False, "Previous score must be between 0 and 100"
        
        if not (4 <= sleep_hours <= 12):
            return False, "Sleep hours must be between 4 and 12"
        
        if not (0 <= attendance <= 100):
            return False, "Attendance must be between 0 and 100%"
        
        return True, {
            'study_hours': study_hours,
            'previous_score': previous_score,
            'sleep_hours': sleep_hours,
            'attendance': attendance
        }
    
    except (ValueError, TypeError):
        return False, "Please enter valid numbers for all fields"

def make_prediction(validated_data):
    """Make prediction using the loaded model"""
    try:
        features = [
            validated_data['study_hours'],
            validated_data['previous_score'],
            validated_data['sleep_hours'],
            validated_data['attendance']
        ]
        
        prediction = model_package['model'].predict([features])[0]
        
        # Ensure realistic score
        prediction = max(0, min(100, prediction))
        
        return round(prediction, 1), None
    
    except Exception as e:
        return None, f"Prediction error: {str(e)}"

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    if model_package is None:
        flash('Model is not available. Please check server logs.', 'error')
        return render_template('index.html')
    
    # Validate input
    is_valid, result = validate_input(request.form)
    if not is_valid:
        flash(f'Input Error: {result}', 'error')
        return render_template('index.html')
    
    # Make prediction
    prediction, error = make_prediction(result)
    if error:
        flash(f'Prediction Error: {error}', 'error')
        return render_template('index.html')
    
    # Success
    flash(f'Predicted Exam Score: {prediction}%', 'success')
    return render_template('index.html', 
                         prediction=prediction,
                         input_data=result)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    if model_package is None:
        return jsonify({'error': 'Model not available'}), 500
    
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    # Validate input
    is_valid, result = validate_input(request.json)
    if not is_valid:
        return jsonify({'error': result}), 400
    
    # Make prediction
    prediction, error = make_prediction(result)
    if error:
        return jsonify({'error': error}), 500
    
    return jsonify({
        'predicted_score': prediction,
        'input_features': result,
        'model_info': model_package['model_type']
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_package is not None
    })

if __name__ == '__main__':
    # Load model on startup
    if load_model():
        print("✅ Model loaded successfully!")
        print("🚀 Starting Flask server...")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("❌ Failed to load model!")
        print("Please run 'python train_model.py' first to create the model.")