# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from crewai import Crew
from app.crew.agents import get_agents
from app.crew.tasks import get_tasks

load_dotenv()

app = FastAPI()


class OptimizeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def health_check():
    return {"status": "OK", "message": "Resume Builder is alive!"}


@app.post("/optimize")
def optimize_resume(req: OptimizeRequest):
    try:
        # Get agents and tasks
        agents = get_agents()
        tasks = get_tasks(agent=agents[0], resume_text=req.resume_text, job_description=req.job_description)

        # ✅ Define crew properly
        my_crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True
        )

        # ✅ Run it
        result = my_crew.kickoff()
        return {"optimized_resume": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
