# Loan_Approval
# Loan Approval Prediction API

This is a simple FastAPI-based API for predicting loan approval status. Given a set of input features such as gender, marital status, income, and credit history, the API predicts whether a loan application is likely to be approved or not.

# Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Input Data Schema](#input-data-schema)
- [Response](#response)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)

# Getting Started

To get started with this API, you'll need to have Python and FastAPI installed on your system. You can install FastAPI using pip:
pip install fastapi

Additionally, ensure you have the trained machine learning model saved in a file (e.g., naive_bayes_model.pkl) in the same directory as the API script.


# Usage
This API allows you to send a POST request with input data and receive a response containing the loan approval status.


# API Endpoints
GET /: A simple welcome message to confirm that the API is running.
POST /predict_loan_approval/: Predicts the loan approval status based on input data.


# Input Data Schema
The input data should be in JSON format and conform to the following schema:

json
{
    "Gender": 0,
    "Married": 1,
    "Dependents": 2,
    "Self_Employed": 1,
    "LoanAmount": 5000.0,
    "Loan_Amount_Term": 360.0,
    "Credit_History": 1.0,
    "ApplicantIncome": 6000.0
}
Gender (0 for Male, 1 for Female)
Married (0 for No, 1 for Yes)
Dependents (Number of dependents)
Self_Employed (0 for No, 1 for Yes)
LoanAmount (Loan amount requested)
Loan_Amount_Term (Loan amount term in months)
Credit_History (Credit history status, 0 or 1)
ApplicantIncome (Applicant's income)


# Response 
The API response will be in JSON format and includes the following fields:
Loan_Approval_Status: Either "Loan Approved" or "Loan Not Approved"
Gender: The gender of the applicant (Male or Female)
Self_Employed: Whether the applicant is self-employed (Yes or No)


# Running the Application
To run the application locally, use the following command:

uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000/docs
