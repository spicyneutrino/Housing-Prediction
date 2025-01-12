from app import app
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
model = joblib.load(MODEL_PATH)

if __name__ == "__main__":
    app.run(debug=True)