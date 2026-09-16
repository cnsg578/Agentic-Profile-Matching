from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    conversation_history: List[str]
    job_description: str
    requirements: Dict
    candidates: List[Dict]
    shortlisted_candidates: List[Dict]
    rankings: List[Dict]
    report: str
    feedback: str
    reasoning: List[str]