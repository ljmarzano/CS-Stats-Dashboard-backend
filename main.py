from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium_automation import download_report
import pandas as pd
import io

app = FastAPI()

# Simulated function to authenticate to the backoffice
def authenticate_to_backoffice(email: str, password: str) -> bool:
    # Simulating a successful login for now
    return email == "test@example.com" and password == "password123"

# Simulated function to fetch a CSV file from the backoffice
def fetch_csv_from_backoffice() -> pd.DataFrame:
    # Simulated CSV data
    csv_data = """Company,Store,Month,Views,Navigations
TEMPLE,Temple A,January 2023,100,50
TEMPLE,Temple A,February 2023,120,55
TEMPLE,Temple B,January 2023,200,80
TEMPLE,Temple B,February 2023,210,85
"""
    return pd.read_csv(io.StringIO(csv_data))

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    if authenticate_to_backoffice(request.email, request.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/fetch-data")
def fetch_data():
    try:
        # Fetching the simulated CSV
        df = fetch_csv_from_backoffice()
        # Returning as JSON
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/download-report")
def download_report_endpoint():
    download_report()
    return {"message": "Reporte descargado con éxito"}
