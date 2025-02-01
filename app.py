from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    RAG: str

insurance_claim_response = {
    "Name": "Jane Doe",
    "PolicyNumber": "ABC123456789",
    "Vehicle Make and Model": "Toyota Camry",
    "Vehicle Year": "2020",
    "License Plate Number": "7XYZ123",
    "Date of Incident": "January 20, 2025",
    "Time of Incident": "3:45 PM",
    "Location of Incident": "Interstate 680, near Exit 40, California",
    "Weather Conditions": "Clear and sunny",
    "Cause of Damage": "Flying pebble hit the windshield",
    "Extent of Damage": "4-inch crack on the driver's side of windshield",
    "Driver's License Number": "CA987654321",
    "State of Driver's License": "California",
    "Insurance Company": "ABC Insurance Company",
    "Contact Information": "555-123-4567",
    "Email Address": "jane.doe@example.com",
    "Incident Description": "While driving on Interstate 680 near Exit 40, a pebble was kicked up by a passing vehicle, causing a crack in the windshield.",
    "Police Report Filed": "No",
    "Photos of Damage": "Yes",
    "Repair or Replacement Needed": "Replacement",
    "Preferred Repair Shop": "Speedy Auto Glass, 123 Glass Street, Pleasant Hill, CA",
    "Deductible Amount": "$100",
    "Witnesses": "None",
    "Other Parties Involved": "None"
}

@app.post("/query")
def get_insurance_claim_details(request: QueryRequest):
    if request.RAG == "insuranceClaimData":
        return insurance_claim_response
    else:
        raise HTTPException(status_code=400, detail="Invalid request")

# Run the application using: uvicorn app:app --host 0.0.0.0 --port 8000