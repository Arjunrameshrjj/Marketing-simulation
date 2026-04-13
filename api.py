from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from engine import DDOMEngine

app = FastAPI(title="DDOM Simulation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Allocation(BaseModel):
    discVar: float
    discFixed: float
    tryVar: float
    tryFixed: float
    buyVar: float
    buyFixed: float
    useVar: float
    useFixed: float
    renewVar: float
    renewFixed: float

class SimulationRequest(BaseModel):
    allocations: List[Allocation]

@app.get("/", response_class=HTMLResponse)
def serve_react_app():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/simulate")
def simulate(request: SimulationRequest):
    engine = DDOMEngine()
    results = []
    
    for alloc_obj in request.allocations:
        # Pydantic 1.x / 2.x safe dict conversion
        alloc_dict = alloc_obj.dict()
        res = engine.simulate(alloc_dict)
        results.append(res)
        
    return {
        "results": results,
        "is_complete": engine.is_complete(),
        "next_quarter": engine.get_current_quarter()
    }
