from langgraph.graph import StateGraph, END
from agent.state import AgentState
from tools.tools import extract_requirements
from rag.rag import rag_search_tool
from tools.explain import generate_explanation


def parse_jd(state: AgentState):
    state["conversation_history"].append(f"Parsed JD: {state['job_description']}")
    return state


def extract_requirements_node(state: AgentState):
    state["requirements"] = extract_requirements(state["job_description"])
    return state


def search_resumes(state: AgentState):
    state["candidates"] = rag_search_tool(state["requirements"])
    return state


def rank_candidates(state: AgentState):
    ranked = sorted(state["candidates"], key=lambda x: x["score"], reverse=True)

    state["rankings"] = ranked
    state["shortlisted_candidates"] = ranked[:10]

    state["reasoning"] = []
    for c in ranked[:10]:
        state["reasoning"].append(
            f"{c['name']} ranked higher due to better skill match."
        )

    return state


def multi_round_selection(state: AgentState):
    for c in state["shortlisted_candidates"]:
        c["deep_score"] = c["score"] + 5
        c["decision"] = "Hire" if c["deep_score"] > 85 else "No Hire"

    return state


def generate_report(state: AgentState):
    report = "\n===== FINAL REPORT =====\n"

    for c in state["shortlisted_candidates"]:
        report += generate_explanation(c)
        report += f"Decision: {c['decision']}\n"
        report += "----------------------\n"

    state["report"] = report
    return state


def human_feedback(state: AgentState):
    feedback = state.get("feedback", "")

    if feedback:
        if "node" in feedback.lower():
            state["requirements"]["must_have"].append("Node.js")

    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("parse_jd", parse_jd)
    graph.add_node("extract_requirements", extract_requirements_node)
    graph.add_node("search_resumes", search_resumes)
    graph.add_node("rank_candidates", rank_candidates)
    graph.add_node("multi_round", multi_round_selection)
    graph.add_node("generate_report", generate_report)
    graph.add_node("human_feedback", human_feedback)

    graph.set_entry_point("parse_jd")

    graph.add_edge("parse_jd", "extract_requirements")
    graph.add_edge("extract_requirements", "search_resumes")
    graph.add_edge("search_resumes", "rank_candidates")
    graph.add_edge("rank_candidates", "multi_round")
    graph.add_edge("multi_round", "generate_report")
    graph.add_edge("generate_report", "human_feedback")
    graph.add_edge("human_feedback", END)

    return graph.compile()