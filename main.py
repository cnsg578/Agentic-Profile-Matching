from agent.matching_agent import build_graph
from tools.tools import compare_candidates, generate_interview_questions


def main():
    graph = build_graph()

    state = {
        "conversation_history": [],
        "job_description": "",
        "requirements": {},
        "candidates": [],
        "shortlisted_candidates": [],
        "rankings": [],
        "report": "",
        "feedback": "",
        "reasoning": []
    }

    print("AI Resume Matching Agent")

    while True:
        user_input = input("\nYou: ")

        if user_input == "exit":
            break

        elif "find" in user_input.lower():
            state["job_description"] = user_input
            state = graph.invoke(state)
            print(state["report"])

        elif "compare" in user_input.lower():
            print(compare_candidates([1, 2, 3]))

        elif "interview" in user_input.lower():
            print(generate_interview_questions("1"))

        elif "why" in user_input.lower():
            for r in state["reasoning"]:
                print(r)

        elif "update" in user_input.lower():
            state["feedback"] = user_input
            state = graph.invoke(state)
            print(state["report"])


if __name__ == "__main__":
    main()