# orchestrate-skill-fastapi
demo skill to return a JSON with a dummy insurance information


## build it

* If you have a mac, then run commands :

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

for win OS in powershell run
```sh
.\.venv\bin\activate
```

pip freeze | grep -E 'fastapi|uvicorn|pydantic' > requirements.txt





Run the application using: 
```sh
uvicorn app:app --host 0.0.0.0 --port 8000

```


## test it

```sh
curl --location 'http://0.0.0.0:8000/query' \
--header 'Content-Type: application/json' \
--data '{"RAG":"insuranceClaimData"}'
```

you should get the following:
```json
{"Name":"Jane Doe","PolicyNumber":"ABC123456789","Vehicle Make and Model":"Toyota Camry","Vehicle Year":"2020","License Plate Number":"7XYZ123","Date of Incident":"January 20, 2025","Time of Incident":"3:45 PM","Location of Incident":"Interstate 680, near Exit 40, California","Weather Conditions":"Clear and sunny","Cause of Damage":"Flying pebble hit the windshield","Extent of Damage":"4-inch crack on the driver's side of windshield","Driver's License Number":"CA987654321","State of Driver's License":"California","Insurance Company":"ABC Insurance Company","Contact Information":"555-123-4567","Email Address":"jane.doe@example.com","Incident Description":"While driving on Interstate 680 near Exit 40, a pebble was kicked up by a passing vehicle, causing a crack in the windshield.","Police Report Filed":"No","Photos of Damage":"Yes","Repair or Replacement Needed":"Replacement","Preferred Repair Shop":"Speedy Auto Glass, 123 Glass Street, Pleasant Hill, CA","Deductible Amount":"$100","Witnesses":"None","Other Parties Involved":"None"}

```