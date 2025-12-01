import streamlit as st
from orchestrator.orchestrator import orchestrator
from orchestrator.agents.expense_agent import ExpenseAgent
from orchestrator.agents.wellness_agent import WellnessAgent

st.set_page_config(layout="wide", page_title="Life Automation Supervisor (LAS)")

st.title("⏳ Life Automation Supervisor (LAS)")
st.markdown("Your AI assistant for meals, calendar, expenses & wellness")

# Initialize session state for result
if 'las_result' not in st.session_state:
    st.session_state.las_result = None

# --- User Goal Input ---
user_goal = st.text_input(
    "What do you want help with?",
    placeholder="Plan my week, meals, workouts, expenses..."
)

if st.button("Run LAS") and user_goal:
    with st.spinner("Running LAS..."):
        result = orchestrator(user_goal, verbose=False)
        st.session_state.las_result = result

# Display results if available
if st.session_state.las_result:
    result = st.session_state.las_result
    
    # --- Meal Display ---
    if "results" in result and "meal" in result["results"]:
        st.subheader("🍽 Meal Plan")
        meal_data = result["results"]["meal"]
        
        if "meal_plan" in meal_data:
            meal_plan = meal_data["meal_plan"]
            
            # Create a nice table view
            cols = st.columns(7)
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            
            for idx, day in enumerate(days):
                if day in meal_plan:
                    with cols[idx]:
                        st.markdown(f"**{day}**")
                        meals = meal_plan[day]
                        
                        # Handle both dict with numeric keys and list
                        if isinstance(meals, dict):
                            # Convert dict to list sorted by keys
                            meal_list = [meals[str(i)] for i in sorted([int(k) for k in meals.keys()])]
                        elif isinstance(meals, list):
                            meal_list = meals
                        else:
                            meal_list = [str(meals)]
                        
                        # Display meals with labels
                        meal_labels = ["🌅 Breakfast", "🌞 Lunch", "🌙 Dinner"]
                        for i, meal in enumerate(meal_list):
                            if i < len(meal_labels):
                                st.markdown(f"{meal_labels[i]}")
                                st.write(meal)
                            else:
                                st.write(meal)
        
        # Display grocery list
        if "grocery_list" in meal_data:
            st.markdown("---")
            st.subheader("🛒 Grocery List")
            grocery_list = meal_data["grocery_list"]
            
            # Handle both dict with numeric keys and list
            if isinstance(grocery_list, dict):
                items = [grocery_list[str(i)] for i in sorted([int(k) for k in grocery_list.keys()])]
            elif isinstance(grocery_list, list):
                items = grocery_list
            else:
                items = []
            
            # Display in columns
            cols = st.columns(4)
            for idx, item in enumerate(items):
                with cols[idx % 4]:
                    st.markdown(f"✓ {item}")
    
    # --- Calendar Display ---
    if "results" in result and "calendar" in result["results"]:
        st.markdown("---")
        st.subheader("📅 Upcoming Events")
        events_data = result["results"]["calendar"]
        
        # Handle dict with numeric keys
        if isinstance(events_data, dict) and "events" not in events_data:
            events = [events_data[str(i)] for i in sorted([int(k) for k in events_data.keys()]) if str(i) in events_data]
        elif isinstance(events_data, dict) and "events" in events_data:
            events = events_data["events"]
        elif isinstance(events_data, list):
            events = events_data
        else:
            events = []
        
        for ev in events:
            if isinstance(ev, dict):
                desc = ev.get("description", "No description")
                start = ev.get("start", "No start time")
                end = ev.get("end", "No end time")
                st.markdown(f"📌 **{desc}** | {start} → {end}")

st.markdown("---")

# --- Expense Tracker ---
st.subheader("💰 Expense Tracker")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**Current Expenses:**")
    try:
        expense_agent = ExpenseAgent()
        expenses = expense_agent.handle("")
        if expenses and len(expenses) > 0:
            st.table(expenses)
        else:
            st.info("No expenses logged yet.")
    except Exception as e:
        st.error(f"Error loading expenses: {e}")

with col2:
    st.markdown("**Log New Expense**")
    with st.form("expense_form", clear_on_submit=True):
        expense_item = st.text_input("Item")
        expense_amount = st.number_input("Amount", min_value=0.0, step=0.01)
        submit_expense = st.form_submit_button("💾 Log Expense")
        if submit_expense and expense_item:
            new_expense = {
                "Item": expense_item,
                "Amount": expense_amount,
            }
            try:
                expense_agent.log_expense(new_expense)
                st.success("✅ Expense logged!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")

# --- Wellness Tracker ---
st.subheader("💪 Wellness Tracker")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**Current Wellness Entries:**")
    try:
        wellness_agent = WellnessAgent()
        wellness = wellness_agent.handle("")
        if wellness and len(wellness) > 0:
            st.table(wellness)
        else:
            st.info("No wellness entries logged yet.")
    except Exception as e:
        st.error(f"Error loading wellness data: {e}")

with col2:
    st.markdown("**Log New Wellness Entry**")
    with st.form("wellness_form", clear_on_submit=True):
        wellness_activity = st.text_input("Activity")
        wellness_duration = st.number_input("Duration (minutes)", min_value=0, step=1)
        submit_wellness = st.form_submit_button("💾 Log Wellness")
        if submit_wellness and wellness_activity:
            new_entry = {
                "Activity": wellness_activity,
                "Duration": wellness_duration,
            }
            try:
                wellness_agent.log_wellness(new_entry)
                st.success("✅ Wellness entry logged!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")