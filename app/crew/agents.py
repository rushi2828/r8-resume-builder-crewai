from crewai import Agent
import os
from dotenv import load_dotenv

load_dotenv()


def get_agents() -> list[Agent]:

    resume_agent = Agent(
        role="Resume Optimizer",
        goal="Craft job-winning, tailored, ATS-friendly resumes",
        backstory=(
            "You're an AI-powered resume consultant helping job-seekers land interviews "
            "by optimizing their resumes to match job descriptions and industry expectations."
        ),
        tools=[],
        verbose=True
    )

    return [resume_agent]
