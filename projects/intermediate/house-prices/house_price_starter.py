# House Price Prediction - Starter Code

"""
House Price Prediction Project
Predict house prices using machine learning algorithms.

TODO: Complete the missing functions and implement the ML pipeline.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

class HousePricePredictor:
    def __init__(self):
        self.models = {}
        self.scaler = StandardScaler()
        self.results = {}
    
    def load_data(self):
        """Load the California housing dataset"""
        # TODO: Load data using sklearn.datasets.fetch_california_housing()
        # Return features and target as pandas DataFrames
        pass
    
    def explore_data(self, df):
        """Perform exploratory data analysis"""
        print("=== DATA EXPLORATION ===")
        print(f"Dataset shape: {df.shape}")
        print("\nDataset info:")
        print(df.info())
        print("\nStatistical summary:")
        print(df.describe())
        
        # TODO: Check for missing values
        # TODO: Visualize target variable distribution
        # TODO: Create correlation heatmap
        
    def create_features(self, df):
        """Engineer new features"""
        # TODO: Create meaningful features like:
        # - bedrooms_per_room = AveBedrms / AveRooms
        # - population_per_household = Population / Households  
        # - income_per_room = MedInc / AveRooms
        pass
    
    def prepare_data(self, X, y):
        """Split and scale the data"""
        # TODO: Split data into train/test sets (80/20)
        # TODO: Scale features using StandardScaler
        # Return X_train, X_test, y_train, y_test (scaled and unscaled)
        pass
    
    def train_models(self, X_train, y_train):
        """Train multiple regression models"""
        # TODO: Initialize and train these models:
        # - Linear Regression
        # - Ridge Regression (alpha=1.0)
        # - Lasso Regression (alpha=1.0)
        # - Random Forest Regressor (n_estimators=100)
        
        # Store trained models in self.models dictionary
        pass
    
    def evaluate_models(self, X_test, y_test):
        """Evaluate all trained models"""
        # TODO: For each model, calculate:
        # - RMSE (Root Mean Square Error)
        # - MAE (Mean Absolute Error)
        # - R² Score
        
        # Store results in self.results dictionary
        pass
    
    def visualize_results(self, y_test):
        """Create visualization plots"""
        # TODO: Create subplots showing:
        # 1. Model performance comparison (bar chart)
        # 2. Actual vs Predicted scatter plots
        # 3. Residual plots
        pass
    
    def predict_price(self, features):
        """Predict house price for new features"""
        # TODO: Use the best performing model to make prediction
        # Return prediction with confidence interval
        pass
    
    def feature_importance(self):
        """Analyze feature importance (for Random Forest)"""
        # TODO: Extract and visualize feature importance
        # Create horizontal bar chart
        pass
    
    def run_complete_pipeline(self):
        """Run the complete ML pipeline"""
        print("🏠 HOUSE PRICE PREDICTION PROJECT")
        print("=" * 50)
        
        # Step 1: Load data
        print("1. Loading data...")
        # TODO: Implement data loading
        
        # Step 2: Explore data
        print("\n2. Exploring data...")
        # TODO: Implement data exploration
        
        # Step 3: Feature engineering
        print("\n3. Engineering features...")
        # TODO: Implement feature engineering
        
        # Step 4: Prepare data
        print("\n4. Preparing data...")
        # TODO: Implement data preparation
        
        # Step 5: Train models
        print("\n5. Training models...")
        # TODO: Implement model training
        
        # Step 6: Evaluate models
        print("\n6. Evaluating models...")
        # TODO: Implement model evaluation
        
        # Step 7: Visualize results
        print("\n7. Creating visualizations...")
        # TODO: Implement visualization
        
        # Step 8: Feature importance
        print("\n8. Analyzing feature importance...")
        # TODO: Implement feature importance analysis
        
        print("\n✅ Pipeline completed successfully!")

def main():
    """Main function"""
    predictor = HousePricePredictor()
    predictor.run_complete_pipeline()
    
    # Interactive prediction example
    print("\n" + "=" * 50)
    print("🔮 INTERACTIVE PREDICTION")
    print("=" * 50)
    print("Enter house details to get price prediction:")
    
    # TODO: Implement interactive prediction interface
    # Ask user for input features and provide prediction

if __name__ == "__main__":
    main()