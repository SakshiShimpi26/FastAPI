from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the Patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="City of the Patient")]
    city:Annotated[str,Field(...,description="City of the Patient")]
    age:Annotated[int,Field(...,description="Age of the Patient",examples=["20"],gt=0)]
    gender:Annotated[Literal['male','female','others'],Field(...,description="Gender of the Patient")]
    height:Annotated[float,Field(...,description="Height of the Patient mtrs",examples=["1.78"],gt=0)]
    weight:Annotated[float,Field(...,description="Weight of the Patient kgs",examples=["45"],gt=0)]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        elif self.bmi<30:
            return "Normal"
        elif self.bmi<60:
            return "Overweight"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="Name of the Patient")]
    city: Annotated[Optional[str], Field(default=None, description="City of the Patient")]
    age: Annotated[Optional[int], Field(default=None, description="Age of the Patient", gt=0)]
    gender: Annotated[Optional[Literal['male','female','others']], Field(default=None, description="Gender of the Patient")]
    height: Annotated[Optional[float], Field(default=None, description="Height of the Patient mtrs", gt=0)]
    weight: Annotated[Optional[float], Field(default=None, description="Weight of the Patient kgs", gt=0)]

# Load data from json file 
def load_data():
    with open("D:/FastAPI/02. Path and Query Parameters/patients.json",'r') as f:
        data = json.load(f)
        return data
    
def save_data(data):
    with open("D:/FastAPI/02. Path and Query Parameters/patients.json",'w') as f:
        json.dump(data,f)

@app.get("/")
def demo():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"message":"A Patient Management System Application About Section"}

@app.post("/create")
def create_patient(patient:Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient data with this ID already exists")

    data[patient.id] = patient.model_dump(exclude=[id])

    save_data(data)
        
    return JSONResponse(status_code=201, content={'message':"Patient Created Successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

