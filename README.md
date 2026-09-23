Day 2 — Agentic AI Foundations and Open-Source Practice
Lab Title

Trace a ReAct run on paper for a multi-step question; prompt an LLM with and without Chain-of-Thought and compare the answers

1. Objective

This project demonstrates and compares three approaches for solving problems:

Direct Prompting
Chain-of-Thought (CoT) Prompting
ReAct Agent

The project also demonstrates self-consistency by running the same Chain-of-Thought prompt multiple times and selecting the majority answer.

2. Technologies Used
Python
Groq API
Python-dotenv
Large Language Model (LLM)
ReAct
Chain-of-Thought Prompting
Self-Consistency
VS Code
3. Project Structure
day2/
│
├── .venv/
├── screenshots/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── config.py
├── tools.py
├── agent.py
├── react_trace.py
├── cot_compare.py
├── self_consistency.py
├── analysis.md
└── README.md

.env contains the API key and should never be uploaded to GitHub.

.venv/ contains the local Python virtual environment and should not be uploaded to GitHub.

4. ReAct Agent

ReAct combines an LLM with tools and an iterative process of:

Thought → Action → Observation → Thought → Action → Observation → Final Answer

For this lab, the ReAct agent uses exactly two tools.

Tool 1 — get_course_fee()

This tool retrieves the fee of a course.

Course	Fee
CS101	Rs. 12,000
AI202	Rs. 18,000
DS303	Rs. 15,000
Tool 2 — calculator()

This tool performs mathematical calculations required by the agent.

5. ReAct Problem

The agent solves the following question:

Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

Calculation
Option 1

CS101 + AI202:

12,000 + 18,000 = 30,000

After a 10% scholarship:

30,000 × 0.90 = 27,000

Therefore:

Option 1 = Rs. 27,000
Option 2

CS101 + AI202 + DS303:

12,000 + 18,000 + 15,000 = 45,000

After a 25% scholarship:

45,000 × 0.75 = 33,750

Therefore:

Option 2 = Rs. 33,750
Difference
33,750 - 27,000 = 6,750

Therefore:

Difference = Rs. 6,750
6. ReAct Agent Trace

The actual agent execution performed the following tool operations:

Step 1:
get_course_fee("CS101")
Observation → 12000

Step 2:
get_course_fee("AI202")
Observation → 18000

Step 3:
get_course_fee("DS303")
Observation → 15000

Step 4:
calculator("12000 + 18000")
Observation → 30000

Step 5:
calculator("30000 * 0.9")
Observation → 27000

Step 6:
calculator("12000 + 18000 + 15000")
Observation → 45000

Step 7:
calculator("45000 * 0.75")
Observation → 33750

Step 8:
calculator("33750 - 27000")
Observation → 6750

The agent initially reached the maximum step limit before producing its final answer. The max_steps value was therefore increased so that the agent had enough steps to complete the final response.

7. Direct Prompting vs Chain-of-Thought

Three problems were tested using two different prompts.

Direct Prompting

The direct prompt asks the model to provide only the final answer without an explanation.

You are a helpful assistant.
Give only the final answer.
Do not explain.
Chain-of-Thought Prompting

The CoT prompt asks the model to provide a numbered step-by-step solution and a final answer.

You are a helpful assistant.
Solve the problem step by step.
Number each step and show the calculation in that step.
After the steps, write the last line exactly as:
Final Answer: <answer>
8. Question 1 — Course Instalment
Problem

A student takes three courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment?

Calculation
Total = 12,000 + 18,000 + 15,000
      = Rs. 45,000

After 15% scholarship:

45,000 × 0.85
= Rs. 38,250

Each instalment:

38,250 ÷ 4
= Rs. 9,562.50
Expected Answer
Rs. 9,562.50 per instalment
9. Question 2 — Computer Sittings
Problem

A lab has 18 computers. In the morning each computer is shared by 2 students, and in the afternoon by 3 students. How many student sittings happen in one day?

Calculation
Morning:
18 × 2 = 36

Afternoon:
18 × 3 = 54

Total:
36 + 54 = 90
Expected Answer
90 student sittings
10. Question 3 — Height Comparison
Problem

Ravi is taller than Kumar. Kumar is taller than Arun. Priya is shorter than Arun. Who is the tallest and who is the shortest?

Comparison
Ravi > Kumar > Arun
Priya < Arun

Therefore:

Priya < Arun < Kumar < Ravi
Answer
Tallest = Ravi
Shortest = Priya

Both the Direct Prompting and Chain-of-Thought responses produced the correct answer for this question.

11. Self-Consistency

Self-consistency was tested by running the same Chain-of-Thought question multiple times.

The question used was the course instalment problem.

Experiment 1
Runs = 5
Temperature = 0.8

Results:

Run 1 → Rs. 9,562.50
Run 2 → Rs. 9,562.50
Run 3 → Rs. 9,562.50
Run 4 → Rs. 9,562.50
Run 5 → Rs. 9,562.50

Majority answer:

Rs. 9,562.50

Majority count:

5/5

The majority answer was correct.

12. Self-Consistency with Temperature = 0

The same experiment was repeated with:

Runs = 5
Temperature = 0

Results:

Run 1 → Rs. 9,562.50
Run 2 → Rs. 9,562.50
Run 3 → Rs. 9,562.50
Run 4 → Rs. 9,562.50
Run 5 → Rs. 9,562.50

All five runs produced the same numerical answer.

For this particular experiment, the majority vote did not change the result.

13. Comparison of the Three Approaches
Feature	Direct Prompting	Chain-of-Thought	ReAct
Output	Final answer	Step-by-step solution	Actions, observations and final answer
Tool usage	No	No	Yes
External information	Not available through tools	Not available through tools	Can obtain information using tools
Calculations	Model-generated	Step-by-step model-generated	Calculator tool
Traceability	Lower	Higher	High
Interaction with environment	No	No	Yes
Suitable for	Simple questions	Multi-step problems using provided information	Problems requiring tools or external information
14. ReAct vs Chain-of-Thought

Chain-of-Thought prompting provides a structured solution when the required information is already present in the question.

ReAct extends this process by allowing the agent to interact with tools.

In the course-fee problem, the agent did not need to assume or invent the course fees. It retrieved them using:

get_course_fee()

It then performed the calculations using:

calculator()

The main distinction observed in this experiment is that ReAct combines an LLM with actions and observations from tools.

15. Self-Consistency Observation

Self-consistency repeats the same problem several times and uses the most common answer.

For this experiment:

Temperature 0.8 → 5/5 = Rs. 9,562.50

Temperature 0   → 5/5 = Rs. 9,562.50

Therefore, the repeated runs produced the same numerical result in both experiments.

This is an observation from this particular experiment and does not imply that all questions will always produce identical results.

16. Main Learning
Direct Prompting

Direct prompting asks the model for the final answer without an explanation.

Chain-of-Thought

Chain-of-Thought prompting asks the model to provide a structured sequence of calculations or steps.

ReAct

ReAct allows an LLM to interact with tools and use the returned observations before producing the final answer.

Self-Consistency

Self-consistency repeats a reasoning task several times and uses the majority answer.

17. How to Run the Project
Step 1 — Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
Step 2 — Run the ReAct trace
python react_trace.py
Step 3 — Run Direct Prompting vs CoT
python cot_compare.py
Step 4 — Run Self-Consistency
python self_consistency.py
18. Python Files
File	Purpose
config.py	Loads environment variables and configures the Groq client
tools.py	Defines the course-fee and calculator tools
agent.py	Implements the ReAct agent
react_trace.py	Runs the ReAct problem and displays the trace
cot_compare.py	Compares Direct Prompting and CoT
self_consistency.py	Runs repeated CoT responses and determines the majority answer
analysis.md	Contains the experiment analysis
README.md	Project documentation
19. Screenshots

The screenshots/ folder contains screenshots of the experiment outputs, including:

ReAct agent trace
Direct Prompting vs CoT output
Self-Consistency with temperature 0.8
Self-Consistency with temperature 0
20. Conclusion

This project demonstrates three different approaches to solving problems with LLMs.

Direct Prompting requests a direct answer.

Chain-of-Thought Prompting requests a structured step-by-step solution.

ReAct adds tool interaction to the LLM workflow, allowing the agent to retrieve information and perform calculations through tools.

The self-consistency experiment demonstrates how repeated model responses can be compared using a majority answer.

The experiments provide a practical demonstration of the progression from simple prompting to tool-using AI agents.