# My To-Do

#### Video Demo: https://youtu.be/vEgEyAwxpjc
#### Description: A Python built Command Line Interface (CLI) based simple task manager.

## General overview

My To-Do is a CLI-based task manager which is entirely built using just python. It uses File I/O to incorporate all the data in a csv file, by default it's `tasks.csv`. Each time the program is executed, the entire csv file is loaded on the computer memory, then all the data are operated and processed, and then the whole file gets rewritten. This design might seem a bit off as all the big programs can not use this strategy as the memory might run out. But, for a simple task manager, this strategy works out just fine. It also proves to be more efficient and reliable not to mess up the file.


## Design strategy and Implimentation

### The Task Class

The program basically runs on tasks and all the tasks are defined by the **Task** class. It has a few attributes:
- **Title:** It's just the title.
- **State:** It stores if the task is done or pending using a boolean value.
- **Priority:** There could be either one of the 3 priorities in a task. "Primary", "Secondary", or "Irrelevant". "Secondary" is the default priority. There's also a property setter to just allow one of the 3 priorities to be allowed.
- **Unique ID:** There's a unique ID assigned to every task. I'm trying but couldn't make it work properly yet, but I'll update the code soon.

Methods of the class:
- **`toggle_done()`:** This method reverses the boolean value of a task's state.
- **`to_dict()`:** It converts the task instance into a dictionary to be written properly in a csv file, presumably `tasks.csv`.
- **`from_dict()`:** This one does the opposit of `to_dict()`, as it creates a task instance from a dictionary.

### The TaskManager Class

The **TaskManager** class is the one that actually interacts with the csv file. It---
- **Loads Tasks:** Gets all the data from the csv file and loads it in the memory as a list of instances using `Task.from_dict()`. This list gets stored in the instance created with the class.
- **Writes Tasks:** Reverses the Task Loading. Gets the list of instances and then stores them in the csv file with the correct structure maintaining the correct schema.
- **Manages Task Operations:** The class has methods for adding a new task, deleting an existing one, toggling a task's completion status, printing all tasks, and displaying details of a specific task.

### Command Line Interface and Modes

The program uses Python's `sys.argv` to receive user commands. You select a mode as the first argument, followed by additional inputs based on the operation. The following modes are supported:
- **`add_task`:** Add a new task with a title and an optional priority.
- **`toggle_done`:** Toggle a task's state (completed/pending) using its title or ID.
- **`del_task`:** Delete a task, identified either by its ID or title.
- **`list_tasks`:** List all tasks with structured output.
- **`task`:** Display detailed information for a specific task.

## Rationale Behind Design Choices

I really liked how bash works on Lynux. So, I tried to have a program that kind of works like bash where you select a mode and then give the arguments to operate and all the other things came from that inspiration. That's why I used matching and you know what, "It totally works."

## Usage Example

Here’s how you might use the program from the command line:

- **Adding a Task:**
  `python file.py add_task "Complete homework" Primary`
  This creates a new task named "Complete homework" with a "Primary" priority.

- **Toggling Task Status:**
  `python file.py toggle_done 1`
  This switches the state of the task with ID 1 from pending to done (or vice versa).

- **Deleting a Task:**
  `python file.py del_task "Complete homework"`
  This removes the task with the title "Complete homework" from the CSV.

- **Listing Tasks:**
  `python file.py list_tasks`
  This command displays all the tasks in a neatly formatted manner.

## Conclusion

Even though I'm submitting my project right now, I don't think it's close to finish yet. I think I can improve it a lot. Making the unique ID work was the biggest challange in this project. It took me three times the time to fix this one bug than coding the rest of the program. Even though this program is super simple, I think a lot more functionalities can be added here and using external packages, it can also be integrated with GUI. So, it has potential and I will be working on it in the future even though my cs50 course is presumably done.
