import numpy as np
from sklearn.linear_model import LinearRegression
from decimal import Decimal

def predict_future(simulation_data):
    """Predict 12 months beyond simulation end"""
    X = np.array([i for i in range(len(simulation_data))]).reshape(-1, 1)
    y = np.array([float(p['total_balance']) for p in simulation_data])
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_months = 12
    future_X = np.array([len(simulation_data) + i for i in range(future_months)]).reshape(-1, 1)
    predictions = model.predict(future_X)
    
    return [Decimal(str(p)) for p in predictions]