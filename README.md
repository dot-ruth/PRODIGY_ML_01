# House Price Prediction

## Description

This project is designed to predict house prices based on user input. It uses machine learning to estimate the price of a house given its square footage, number of bedrooms, and number of bathrooms. The application features a user-friendly interface built with Vue.js and a robust backend developed with Flask.

## Tech Stack

- **Frontend:**
  - **Vue.js**: A progressive JavaScript framework used to build the user interface and handle user interactions.

- **Backend:**
  - **Flask**: A lightweight Python web framework used to create the API that serves predictions.
  - **joblib**: Used to serialize and deserialize the trained machine learning model.
  - **numpy**: Used for numerical operations and preparing data for model predictions.

- **Machine Learning:**
  - **Scikit-learn**: A Python library used to train and predict house prices using linear regression.

## Project Structure

- **Frontend (Vue.js)**: Provides a responsive and interactive UI for users to input house details and view predicted prices.
- **Backend (Flask)**: Handles HTTP requests, performs predictions using the trained model, and responds with the predicted house price.
