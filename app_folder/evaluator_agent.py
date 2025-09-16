# evaluator_agent.py
from pydantic import BaseModel, Field
from typing import List
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ["GOOGLE_API_KEY"]
)

gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=gemini_client)

class EvaluationFeedback(BaseModel):
    suggestions: List[str] = Field(description="Suggestions to improve the research report")

INSTRUCTIONS = """
You are a critical reviewer. Evaluate the quality, clarity, completeness, and relevance of the research report.
Identify any gaps, factual inconsistencies, or vague sections. Provide concise suggestions to improve it.
"""

evaluator_agent = Agent(
    name="EvaluatorAgent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=EvaluationFeedback,
)
