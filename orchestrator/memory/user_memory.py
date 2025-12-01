# orchestrator/memory/user_memory.py
import json
import os

MEM_FILE = "user_memory.json"

def load_memory():
    if os.path.exists(MEM_FILE):
        with open(MEM_FILE) as f:
            return json.load(f)
    return {"preferences": {}, "history": []}

def save_memory(mem):
    with open(MEM_FILE, "w") as f:
        json.dump(mem, f, indent=2)
