# optimizer_agent.py
from pydantic import BaseModel, Field
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ["GOOGLE_API_KEY"]
)

gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=gemini_client)


class OptimizedReport(BaseModel):
    improved_markdown_report: str = Field(description="Refined research report based on evaluator feedback")

INSTRUCTIONS = """
You are an expert writer. Improve the research report based on evaluator suggestions.
Ensure the revised version is well-structured, concise, and includes relevant improvements.
"""

optimizer_agent = Agent(
    name="OptimizerAgent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=OptimizedReport,
)
