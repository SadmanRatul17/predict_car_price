
# What is My Car Worth?

This repository contains a project aimed at predicting the resale value of a car using Linear Regression. It helps answer the question: "If I want to sell my car, what should I expect to earn?" The project also includes a web application built with the Flask framework for an interactive and user-friendly experience.



## Table of Contents

1.Introduction   
2.Dataset  
3.Features  
4.Project Workflow  
5.Modeling Techniques  
6.Flask Integration  
7.Results  
8.Requirements  

## Dataset
The dataset used for this project includes features that significantly influence car prices, such as:

1.Company: Brand of the car  
2.Model: Specific car model   
3.Year: year of purchase  
4.Fuel Type: Petrol, diesel, or LPG  
5.Mileage: Total distance traveled


## Features
Input Features:

- Company name
- Model of car
- year of purchase
- Fuel_type
- Mileage


## Target:
- Price: The estimated price of the car.
## Project Workflow
1.Data Preprocessing: Clean and prepare the dataset for training.     
2.Model Training: Train a Linear Regression model on the processed data.   
3.Evaluation: Test the model and assess its performance.         
4.Web Integration: Develop a Flask-based web interface for user interaction.    
5.Deployment: Host the application for public access.
## Modeling Techniques
- Linear Regression is used as the primary machine learning model for prediction.
## Flask Integration
The project includes a web application developed using the Flask framework, allowing users to:

- Input car details via a web form.
- Get real-time price predictions.
- Interact with a user-friendly interface.
## Results
- Model Performance: Provide metrics like R^2 and RMSE.
- Web Application: Fully functional interface for price prediction.
## Requirements
- Python 
- Flask
- NumPy
- pandas
- scikit-learn
