class MealAgent:
    def handle(self, goal):
        # Replace this with Gemini API integration later
        meal_plan = {
            "Mon": ["Oatmeal", "Salad", "Grilled Chicken"],
            "Tue": ["Eggs", "Soup", "Fish"],
            "Wed": ["Smoothie", "Sandwich", "Pasta"],
            "Thu": ["Pancakes", "Salad", "Chicken Stir-fry"],
            "Fri": ["Yogurt", "Wrap", "Salmon"],
            "Sat": ["Omelette", "Quinoa Bowl", "Pizza"],
            "Sun": ["French Toast", "Veggie Stir-fry", "Roast Chicken"]
        }
        grocery_list = ["Oats", "Eggs", "Chicken", "Salad", "Fish", "Pasta", "Veggies", "Cheese"]
        return {"meal_plan": meal_plan, "grocery_list": grocery_list}
