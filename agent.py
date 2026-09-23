"""
Day 2 - ReAct Agent

The agent can use:
1. get_course_fee(course_code)
2. calculator(expression)
"""

import json

from config import client, MODEL
from tools import get_course_fee, calculator


SYSTEM_PROMPT = """
You are a ReAct-style course fee assistant.

You have exactly two tools:

1. get_course_fee(course_code)
   - Gets the fee of a course.
   - Valid course codes: CS101, AI202, DS303.

2. calculator(expression)
   - Performs arithmetic calculations.

Rules:
- You do not know course fees unless you use get_course_fee.
- Never invent a course fee.
- Use calculator for ALL arithmetic.
- Do not perform arithmetic mentally.
- When multiple course fees are independently needed, request their
  fee lookups.
- After getting the observations, use calculator to calculate the
  required totals, discounts and differences.
- Give a concise final answer after the required calculations.
"""


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202 or DS303"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


def execute_tool(name, arguments):
    """Execute the requested tool."""

    if name == "get_course_fee":
        return get_course_fee(arguments["course_code"])

    if name == "calculator":
        return calculator(arguments["expression"])

    return f"Unknown tool: {name}"


def agent(question, max_steps=8):
    """
    Run the ReAct agent.

    Returns the final answer from the LLM.
    """

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        assistant_message = response.choices[0].message

        # Add the assistant response to the conversation.
        messages.append(assistant_message)

        # No tool calls means the agent has produced its final answer.
        if not assistant_message.tool_calls:
            return assistant_message.content.strip()

        # Execute each requested tool call.
        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(tool_call.function.arguments)

            print(f"step {step}: {tool_name} {arguments}")

            result = execute_tool(tool_name, arguments)

            print(f"step {step}: observation -> {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "The agent reached the maximum number of steps."


if __name__ == "__main__":

    question = (
        "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
        "or all three courses with a 25% scholarship? By how much?"
    )

    print("QUESTION:", question)
    print()

    answer = agent(question)

    print()
    print("FINAL ANSWER:", answer)