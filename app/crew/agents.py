from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # ✅ Not "gpt-4"
    temperature=0.7
)

def get_agents() -> list[Agent]:
    # Use GPT-3.5 which is available on all OpenAI accounts
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", # ✅ Not "gpt-4"
        temperature=0.7
    )

    resume_agent = Agent(
        role="Resume Optimizer",
        goal="Craft job-winning, tailored, ATS-friendly resumes",
        backstory=(
            "You're an AI-powered resume consultant helping job-seekers land interviews "
            "by optimizing their resumes to match job descriptions and industry expectations."
        ),
        
        llm=llm,
        tools=[],  # No external tools for now to avoid dependency issues
        verbose=True
    )

    return [resume_agent]
