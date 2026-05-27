# My To-Do

#### Video Demo: [https://youtu.be/vEgEyAwxpjc](https://youtu.be/vEgEyAwxpjc)

#### Description: A Python built Command Line Interface (CLI) based simple task manager.

---

## ⚠️ Copyright Notice

**© 2026 Syed Navid Nowroz. All rights reserved.**

This project is **not open source**. No part of this code may be reproduced, distributed, or used without explicit written permission from the copyright holder.

**For cs50Python students:** This repository is for personal portfolio purposes only. Do not copy this code for your own assignment. Learning happens when you build your own solution!

---

## General Overview

My To-Do is a CLI-based task manager which is entirely built using just Python. It uses File I/O to store all the data in a CSV file (by default `tasks.csv`). Each time the program is executed, the entire CSV file is loaded into memory,processed,and then rewritten. This design works well for a simple task manager.

---

## Design Strategy and Implementation

### The Task Class

The program runs on tasks defined by the **Task** class. Attributes:

- **Title:** The task name
- **State:** Boolean (done/pending)
- **Priority:** "Primary", "Secondary" (default), or "Irrelevant"
- **Unique ID:** Unique identifier for each task

**Methods:**
- `toggle_done()` — Reverses the boolean state
- `to_dict()` — Converts task to dictionary for CSV
- `from_dict()` — Creates task instance from dictionary

### The TaskManager Class

The **TaskManager** class interacts with the CSV file:

- **Loads Tasks:** Reads CSV and loads instances using `Task.from_dict()`
- **Writes Tasks:** Stores the list back to CSV with correct schema
- **Manages Task Operations:** Add, delete, toggle completion, print all tasks, display task details

### Command Line Interface and Modes

Uses Python's `sys.argv` to receive commands. Supported modes:

- `add_task` — Add a new task with title and optional priority
- `toggle_done` — Toggle a task's state using title or ID
- `del_task` — Delete a task by ID or title
- `list_tasks` — List all tasks with structured output
- `task` — Display detailed information for a specific task

---

## Rationale Behind Design Choices

I was inspired by how bash works on Linux—select a mode, then give arguments. That's why I used `match` statements. It works 
