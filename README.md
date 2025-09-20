# 📚 Study Hours Predictor

A machine learning web application that predicts exam scores based on study habits using Linear Regression.

🚀 Live Demo
🌐 View Live App https://study-predictor-production.up.railway.app/

## 📋 Features

- **Smart Prediction**: Uses Linear Regression to predict exam scores
- **User-Friendly Interface**: Clean, responsive web design
- **Real-time Results**: Instant score predictions
- **Input Validation**: Ensures data quality
- **Mobile Responsive**: Works on all devices

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **ML Library**: Scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: Pandas, NumPy
- **Deployment**: Render/Railway

## 📊 Model Details

- **Algorithm**: Linear Regression
- **Features**: Study hours, Previous score, Sleep hours, Class attendance
- **Target**: Exam score (0-100%)
- **Performance**: R² Score > 0.85
- **Dataset**: 1000 synthetic student records

## 🏗️ Project Structure

```
study_hours_predictor/
├── app.py                  # Flask web application
├── train_model.py          # ML model training script  
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── templates/
│   ├── base.html          # Base HTML template
│   └── index.html         # Main page
├── static/
│   └── style.css          # CSS styles (if separate)
└── models/
    └── study_model.pkl    # Trained ML model
```

## ⚡ Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/sahil13082003/study-hours-predictor.git
cd study-hours-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python train_model.py
```

### 4. Run the App
```bash
python app.py
```

### 5. Open Browser
Visit: `http://localhost:5000`

## 🌐 Deployment

### Deploy on Render (Free)
1. Fork this repository
2. Go to [render.com](https://render.com)
3. Create new Web Service from GitHub
4. Set build command: `pip install -r requirements.txt && python train_model.py`
5. Set start command: `python app.py`
6. Deploy! 🚀

### Deploy on Railway (Free)
1. Fork this repository  
2. Go to [railway.app](https://railway.app)
3. Deploy from GitHub repository
4. Auto-deploys in minutes! ⚡

## 📖 How to Use

1. **Enter Study Hours**: Daily study time (0-12 hours)
2. **Previous Score**: Your last exam percentage (0-100%)
3. **Sleep Hours**: Nightly sleep duration (4-12 hours) 
4. **Class Attendance**: Attendance percentage (0-100%)
5. **Click Predict**: Get your predicted exam score!

## 🎯 Example Predictions

| Study Hours | Previous Score | Sleep Hours | Attendance | Predicted Score |
|-------------|---------------|-------------|------------|-----------------|
| 8.0         | 85%           | 8.0         | 95%        | ~88% |
| 3.0         | 60%           | 6.0         | 70%        | ~65% |
| 10.0        | 90%           | 7.0         | 98%        | ~92% |

## 🔧 API Usage

### Endpoint
```
POST /api/predict
```

### Request Body
```json
{
  "study_hours": 8.0,
  "previous_score": 85.0,
  "sleep_hours": 8.0,
  "attendance": 95.0
}
```

### Response
```json
{
  "predicted_score": 87.5,
  "input_features": {
    "study_hours": 8.0,
    "previous_score": 85.0,
    "sleep_hours": 8.0,
    "attendance": 95.0
  },
  "model_info": "Linear Regression"
}
```

## 📈 Model Performance

- **Training R² Score**: 0.89
- **Testing R² Score**: 0.85  
- **Mean Squared Error**: 12.34
- **Features Impact**:
  - Study Hours: +4.2 points per hour
  - Previous Score: +0.25 multiplier
  - Sleep Hours: +1.8 points per hour
  - Attendance: +0.15 points per %

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b new-feature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push branch: `git push origin new-feature`
5. Submit Pull Request


⭐ **Star this repository if you found it helpful!**
