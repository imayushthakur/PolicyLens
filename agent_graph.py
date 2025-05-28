from langgraph.graph import StateGraph
from typing import TypedDict
from agents import document_parser, simplifier, query_handler, personalizer, feedback_collector

class AgentState(TypedDict, total=False):
    pdf: object
    query: str
    raw_text: str
    simplified_text: str
    answer: str
    Explanation: str
    Personalized_Tip: str
    Relevant_Clause: str
    profile: dict  # <-- Add this

# For Complete Code, contact : thehaurusai@gmail.com
