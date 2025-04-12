
from crewai import Task
from crewai.agent import Agent


def get_tasks(agent: Agent, resume_text: str, job_description: str ) -> list[Task]:
    task = Task(
        description=(
        "Take this resume:\n\n"
        f"{resume_text}\n\n"
        "And optimize it based on the following job description:\n\n"
        f"{job_description}\n\n"
        "Make it more tailored, keyword-optimized, and ATS-friendly."
        ),
        expected_output="An improved version of the resume, in plain text format.",
        agent=agent
      )

    return [task]