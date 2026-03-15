import os
from groq import Groq
from config import LLM_MAX_TOKENS


def build_prompt(context: str, query: str) -> str:
    return f"""You are a university assistant chatbot.

IMPORTANT RULES:
1. Extract the answer EXACTLY from the context provided.
2. Do NOT rewrite or paraphrase.
3. Do NOT summarize.
4. Copy the exact sentence(s) from the context that answer the question.
5. If the answer is not found, respond with: "Not available in university document."

Context:
{context}

Question:
{query}"""


def get_answer(context: str, query: str) -> str:
    try:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            return "❌ GROQ_API_KEY is not set in Space secrets."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful university assistant. Answer only from the given context."
                },
                {
                    "role": "user",
                    "content": build_prompt(context, query)
                }
            ],
            max_tokens=LLM_MAX_TOKENS,
            temperature=0.1
        )

        answer = response.choices[0].message.content.strip()
        return answer

    except Exception as e:
        return f"❌ LLM error: {e}"