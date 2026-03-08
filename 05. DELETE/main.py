from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal, Optional
import json

app = FastAPI()

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

@app.delete("/delete/{patient_id}")
def delete_data(patient_id:str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Data Not Found")

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content="Data Deleted Successfully")