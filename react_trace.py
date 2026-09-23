"""
Day 2 - Part D
Print the agent's real ReAct trace.
"""

from agent import agent


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)


print("QUESTION:", QUESTION)
print()
print("--- THE AGENT'S ACTIONS AND OBSERVATIONS ---")

answer = agent(QUESTION, max_steps=10)

print()
print("FINAL ANSWER:", answer)