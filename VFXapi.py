from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="Houdini VFX API",
    description="API for handling Houdini simulations, including Pop Dop simulations.",
    version="1.0.0"
)

# Sample data structure for a Houdini Pop Dop Simulation
class PopDopSimRequest(BaseModel):
    particle_count: int
    birth_rate: float
    velocity: Dict[str, float]
    turbulence: float

class PopDopSimResponse(BaseModel):
    message: str
    sim_id: str
    parameters: Dict[str, Any]

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Houdini VFX API"}

@app.post("/pop_dop_sim", response_model=PopDopSimResponse, tags=["POP DOP Sim"])
def create_pop_dop_sim(request: PopDopSimRequest):
    """
    Creates a POP DOP Simulation in Houdini with the specified parameters.
    """
    sim_id = "sim_12345"  # Mocked Sim ID (in reality, integrate with Houdini's API)
    
    response = {
        "message": "Pop Dop Simulation Created Successfully",
        "sim_id": sim_id,
        "parameters": {
            "particle_count": request.particle_count,
            "birth_rate": request.birth_rate,
            "velocity": request.velocity,
            "turbulence": request.turbulence,
        }
    }
    return response

@app.get("/pop_dop_sim/{sim_id}", tags=["POP DOP Sim"])
def get_pop_dop_sim(sim_id: str):
    """
    Retrieves details about a specific Pop Dop Simulation.
    """
    # Mocked response (in reality, fetch data from Houdini or a database)
    return {
        "sim_id": sim_id,
        "status": "Running",
        "particle_count": 10000,
        "birth_rate": 500.0,
        "velocity": {"x": 0.0, "y": 1.5, "z": 0.0},
        "turbulence": 0.25
    }

@app.delete("/pop_dop_sim/{sim_id}", tags=["POP DOP Sim"])
def delete_pop_dop_sim(sim_id: str):
    """
    Deletes a specific Pop Dop Simulation.
    """
    # Mocked deletion response
    return {"message": f"Simulation {sim_id} deleted successfully"}
