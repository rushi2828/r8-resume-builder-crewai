from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.crew.agents import get_agents
from app.crew.tasks import get_tasks
from dotenv import load_dotenv # type: ignore
import os

load_dotenv() # load .env file

app = FastAPI(
    title= "r8 Resume Builder (CrewAI Powered)",
    description= "Optimize resumes using AI agents",
    version= "1.0.0"
)

class OptimizeRequest(BaseModel):
    resume_text: str
    job_description: str

@app.get("/")
def health_check():
    return {"status": "OK", "message":"Resume Builder API running 🚀"}

@app.post("/optimize")
def optimise_resume(request: OptimizeRequest):
    try:
        # Load your CrewAI agent
        agents = get_agents()
        resume_agent = agents[0]

        # Build tasks using resume & job description
        tasks = get_tasks(resume_agent, request.resume_text, request.job_description)

        # Create crew and run
        crew = crew(
            agents=[resume_agent],
            tasks=tasks,
            verbose=True
        )

        result = crew.run()
        return {"optimized_resume": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # # Placeholder for optimization trigger
    # return {"message": "Resume optimization will go here!"}




