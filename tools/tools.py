def extract_requirements(jd: str):
    return {
        "must_have": ["React", "3+ years"],
        "nice_to_have": ["Node.js"]
    }


def compare_candidates(candidate_ids):
    return f"Comparing candidates: {candidate_ids}"


def generate_interview_questions(candidate_id):
    return [
        "Explain React lifecycle",
        "What is useEffect?",
    ]