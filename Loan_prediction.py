from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the trained Naive Bayes model
with open('naive_bayes_model.pkl', 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)

app = FastAPI()

class LoanData(BaseModel):
    # Define the input data schema here
    Gender: int
    Married: int
    Dependents: int
    Self_Employed: int
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    ApplicantIncome: float
    

@app.get("/")
def index():
    return {"message": "Hello There!"}

@app.post("/predict_loan_approval/")
async def predict_loan_approval(data: LoanData):
    # Convert input data to a numpy array
    input_data = np.array([[data.Gender, data.Married, data.Dependents, data.Self_Employed, data.LoanAmount, data.Loan_Amount_Term, data.Credit_History, data.ApplicantIncome]])

    # Use the loaded Naive Bayes model to make predictions
    predictions = naive_bayes_model.predict(input_data)

    # Mapped the predictions to human-readable labels (e.g., "No" or "Yes")
    approval_status = "Loan Approved" if predictions[0] == 1 else "Loan Not Approved"

    
    gender_label = "Female" if data.Gender == 1 else "Male" 
    self_employed_label = "No" if data.Self_Employed == 0 else "Yes"
    
    return {"Loan_Approval_Status": approval_status}

if __name__ == "__Loan_prediction__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)