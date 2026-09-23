"""
Day 2 - Part C
Self-consistency using multiple Chain-of-Thought runs.
"""

from collections import Counter

from config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS


RUNS = 5
TEMPERATURE = 0


def final_answer(text):
    """
    Extract the final answer from the model response.
    """

    for line in reversed(text.splitlines()):
        if "final answer" in line.lower():
            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip() if text.strip() else "(empty)"


def run_many(question, runs=RUNS, temperature=TEMPERATURE):

    answers = []

    for attempt in range(1, runs + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature,
        )

        answer = final_answer(
            response.choices[0].message.content
        )

        print(f"run {attempt}: {answer}")

        answers.append(answer)

    return answers


if __name__ == "__main__":

    banner("SELF-CONSISTENCY")

    question = QUESTIONS[0]

    print("QUESTION:")
    print(question)
    print()

    answers = run_many(question)

    winner, count = Counter(answers).most_common(1)[0]

    print()
    print(f"Majority answer ({count} of {len(answers)} runs): {winner}")