# Housing Price Prediction

A Flask-based web application that predicts house prices based on user input. The application uses a trained machine learning model to make predictions.

## Features
- Predicts house prices based on various input features such as area, bedrooms, bathrooms, and more.
- Machine learning pipeline with preprocessing, feature engineering, and model selection.
- User-friendly interface built with Flask and HTML/CSS.

## Dataset
**Source:** [Kaggle Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)  
**Description:** This dataset contains features such as area, bedrooms, bathrooms, and other attributes of houses, along with their respective prices.

## Machine Learning Model
The application uses a **LightGBM Regressor**, selected after training and evaluating the following models:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- LightGBM Regressor

### Preprocessing Pipeline
- **Numerical Features:** Scaled using `MinMaxScaler`.
- **Categorical Features:**
  - Ordinal features encoded using `OrdinalEncoder`.
  - Nominal features encoded using `OneHotEncoder`.

### Model Selection Process
- A `Pipeline` was used to combine preprocessing and model training steps.
- Hyperparameter tuning was performed using `GridSearchCV` with 5-fold cross-validation.
- Metrics used for evaluation included:
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Squared Logarithmic Error (MSLE)**

## Results
- The **LightGBM Regressor** was the best-performing model with optimized hyperparameters.
- The model achieved an **R² score of 0.6** on the test dataset.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/spicyneutrino/Housing-Prediction.git
    cd Housing-Prediction
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```
    Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Demo
Below is a demo of the Flask application in action:

![Flask App Demo](https://raw.githubusercontent.com/spicyneutrino/Housing-Prediction/refs/heads/main/HousingPricePrediction.gif)

## Deployment
This project is suitable for deployment on **Heroku**.

## Future Improvements
- **Enhanced User Interface:** Improve the web design for a more modern and intuitive experience.
- **Additional Features:** Incorporate more house attributes such as proximity to schools or public transport.
- **Model Expansion:** Experiment with other advanced models or ensemble techniques for improved accuracy.
- **API Integration:** Develop APIs to allow external applications to interact with the prediction service.
- **Cloud Deployment:** Deploy the application on other platforms like AWS or Azure for scalability.

## Acknowledgments
- **Dataset:** [Kaggle Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
- **Technologies:** Flask, Python, and Scikit-Learn.
- Machine learning model tuned with **LightGBM** and **GridSearchCV**.
