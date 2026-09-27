KNOWLEDGE = {
    "python": "Python is a high-level, general-purpose programming language.",
    "fastapi": "FastAPI is a Python framework for building APIs.",
    "jev": "Jev is a decision-making system designed to answer structured questions.",
    "api": "An API is an interface that allows different software systems to communicate."
}


def knowledge_tool(query: str):

    query_lower = query.lower()

    for keyword, answer in KNOWLEDGE.items():

        if keyword in query_lower:
            return answer

    return "I don't have information about that topic yet."