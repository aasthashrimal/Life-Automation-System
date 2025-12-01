from orchestrator.agents.meal_agent import MealAgent
from orchestrator.agents.calendar_agent import CalendarAgent
from orchestrator.agents.expense_agent import ExpenseAgent
from orchestrator.agents.wellness_agent import WellnessAgent
from orchestrator.memory.user_memory import load_memory, save_memory

def orchestrator(goal: str, verbose=False):
    tasks = detect_tasks(goal)
    mem = load_memory()
    results = {}

    plan = {"tasks": []}

    for t in tasks:
        if t == "meal":
            plan["tasks"].append({"agent": "MealAgent", "input": goal})
            output = MealAgent().handle(goal)
            results["meal"] = output

        if t == "calendar":
            plan["tasks"].append({"agent": "CalendarAgent", "input": goal})
            output = CalendarAgent().handle(goal)
            results["calendar"] = output

        if t == "expenses":
            plan["tasks"].append({"agent": "ExpenseAgent", "input": goal})
            output = ExpenseAgent().handle(goal)
            results["expenses"] = output

        if t == "wellness":
            plan["tasks"].append({"agent": "WellnessAgent", "input": goal})
            output = WellnessAgent().handle(goal)
            results["wellness"] = output

    save_memory(mem)
    return {"plan": plan, "results": results, "memory_after": mem}


def detect_tasks(goal: str):
    goal = goal.lower()
    tasks = []
    if any(x in goal for x in ["meal", "food", "diet", "cook"]):
        tasks.append("meal")
    if any(x in goal for x in ["meeting", "schedule", "calendar", "event"]):
        tasks.append("calendar")
    if any(x in goal for x in ["expense", "budget", "money", "spend"]):
        tasks.append("expenses")
    if any(x in goal for x in ["workout", "gym", "fitness", "health"]):
        tasks.append("wellness")
    return tasks
