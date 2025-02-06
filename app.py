from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    RAG: str

insurance_claim_response = {
    "Name": "Jane Doe",
    "PolicyNumber": "ABC123456789",
    "VehicleMakeAndModel": "Toyota Camry",
    "VehicleYear": "2020",
    "LicensePlateNumber": "7XYZ123",
    "DateOfIncident": "February 6, 2025",
    "TimeOfIncident": "7:45 AM",
    "LocationOfIncident": "Interstate 680, near Exit 40, California",
    "WeatherConditions": "Clear and sunny",
    "CauseOfDamage": "Flying pebble hit the windshield",
    "ExtentOfDamage": "can't assess the size of a crack on a windshield; request shop to bring the replacement glass",
    "DriverLicenseNumber": "CA987654321",
    "StateOfDriverLicense": "California",
    "InsuranceCompany": "ABC Insurance Company",
    "ContactInformation": "555-123-4567",
    "EmailAddress": "ad.ibm.automation@gmail.com",
    "IncidentDescription": "While driving on Interstate 680 near Exit 40, a pebble was kicked up by a passing vehicle, causing a crack in the windshield.",
    "PoliceReportFiled": "No",
    "PhotosOfDamage": "Yes",
    "RepairOrReplacementNeeded": "Replacement",
    "PreferredRepairShop": "Speedy Auto Glass, 123 Glass Street, Santa Clara, CA",
    "DeductibleAmount": "$100",
    "Witnesses": "None",
    "OtherPartiesInvolved": "None"
}


@app.post("/query")
def get_insurance_claim_details(request: QueryRequest):
    if request.RAG == "insuranceClaimData":
        return insurance_claim_response
    else:
        raise HTTPException(status_code=400, detail="Invalid request")

# Run the application using: uvicorn app:app --host 0.0.0.0 --port 8000