# Day 2 — Agentic AI Comparison

## 1. Objective

This lab compares three approaches to solving problems:

1. Direct Prompting
2. Chain-of-Thought (CoT) Prompting
3. ReAct Agent

The experiments also include a self-consistency test using repeated CoT runs.

---

## 2. ReAct Experiment

### Question

Which is cheaper: CS101 and AI202 with a 10% scholarship,
or all three courses with a 25% scholarship? By how much?

### Course fees

- CS101 = Rs. 12,000
- AI202 = Rs. 18,000
- DS303 = Rs. 15,000

### Actual agent trace

The agent performed these tool calls:

1. `get_course_fee("CS101")` → Rs. 12,000
2. `get_course_fee("AI202")` → Rs. 18,000
3. `get_course_fee("DS303")` → Rs. 15,000
4. `calculator("12000 + 18000")` → Rs. 30,000
5. `calculator("30000 * 0.9")` → Rs. 27,000
6. `calculator("12000 + 18000 + 15000")` → Rs. 45,000
7. `calculator("45000 * 0.75")` → Rs. 33,750
8. `calculator("33750 - 27000")` → Rs. 6,750

### Final result

CS101 + AI202 with a 10% scholarship costs Rs. 27,000.

All three courses with a 25% scholarship cost Rs. 33,750.

Difference = Rs. 6,750.

Therefore, the first option is cheaper by Rs. 6,750.

---

## 3. Direct Prompting vs Chain-of-Thought

Three questions were tested using:

- Direct prompting: final answer only
- Chain-of-Thought prompting: numbered steps and calculations

### Question 1 — Course instalment

Expected answer:

Rs. 9,562.50 per instalment.

Calculation:

Total = Rs. 45,000

After 15% scholarship:

Rs. 45,000 × 0.85 = Rs. 38,250

Each instalment:

Rs. 38,250 ÷ 4 = Rs. 9,562.50

### Question 2 — Computer sittings

Expected answer:

90 student sittings.

Calculation:

Morning = 18 × 2 = 36

Afternoon = 18 × 3 = 54

Total = 36 + 54 = 90

### Question 3 — Height comparison

Both approaches produced:

- Tallest = Ravi
- Shortest = Priya

The CoT response explicitly showed the comparison chain:

Priya < Arun < Kumar < Ravi

---

## 4. Self-Consistency Experiment

Question 1 was run five times using CoT with temperature = 0.8.

Results:

- Run 1 → Rs. 9,562.50
- Run 2 → Rs. 9,562.50
- Run 3 → Rs. 9,562.50
- Run 4 → Rs. 9,562.50
- Run 5 → Rs. 9,562.50

Majority answer:

Rs. 9,562.50 (5/5)

The majority answer was correct.

### Temperature = 0

The same question was then run five times with temperature = 0.

Results:

- Run 1 → Rs. 9,562.50
- Run 2 → Rs. 9,562.50
- Run 3 → Rs. 9,562.50
- Run 4 → Rs. 9,562.50
- Run 5 → Rs. 9,562.50

All five runs produced the same numerical answer.

For this experiment, the majority vote did not change the result.

---

## 5. Comparison

| Feature | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Output | Final answer | Step-by-step answer | Tool actions + observations + final answer |
| External tools | No | No | Yes |
| Multi-step calculation | Can be requested | Explicitly shown | Performed through calculator |
| Access to external/course data | No | No | Yes, through tools |
| Traceability | Low | Higher | High |
| Tool interaction | None | None | Yes |
| Best suited for | Simple questions | Multi-step reasoning from given information | Problems requiring tools or external information |

---

## 6. ReAct vs Chain-of-Thought

Chain-of-Thought can solve problems when all required information is already available in the prompt.

ReAct adds an important component: tool interaction.

In the course-fee problem, the agent did not need to invent the course fees. It obtained them through:

`get_course_fee()`

It then used:

`calculator()`

for the arithmetic.

Therefore, the important difference observed in this lab is that ReAct combines language-model reasoning with actions and observations from tools.

---

## 7. Self-Consistency Observation

Self-consistency repeats a reasoning process several times and uses the majority answer.

In this experiment:

- Temperature 0.8 → 5/5 produced Rs. 9,562.50
- Temperature 0 → 5/5 produced Rs. 9,562.50

Thus, for this particular problem, the repeated runs did not produce different numerical answers.

---

## 8. Conclusion

Direct prompting, Chain-of-Thought prompting, and ReAct provide different ways to solve problems.

Direct prompting requests the final answer directly.

Chain-of-Thought prompting asks for a structured step-by-step solution.

ReAct extends the process by allowing the model to interact with tools and use their observations before producing the final answer.

The experiments show that the choice of approach depends on the problem. Problems that only require information already provided can be handled through prompting, while problems requiring external information or tool operations benefit from an agent that can perform actions and use observations.