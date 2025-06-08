# Doing the importing stuff
import sys
import csv
import os


# defining the Task class
class Task:
    # class variables
    _id_counter = 1
    priorities = ["Primary", "Secondary", "Irrelevant"]

    def __init__(self, title: str, priority: str = "Secondary", state=False, file_path: str = "tasks.csv"):
        self.title = title
        self.state = state
        self.priority = priority
        if not os.path.exists(file_path):
            self.id = Task._id_counter
            Task._id_counter += 1
        else:
            with open(file_path, "r", newline="", encoding="utf-8") as File:
                reader = csv.DictReader(File)
                rows = list(reader)
                true_ids = {int(x["id"]) for x in rows}
                row_count = len(rows)
                possible_ids = {int(x) for x in range(row_count+2)}
                options = possible_ids - true_ids
                options = options - {0}
                if options:
                    Task._id_counter = min(options)
                    self.id = Task._id_counter
                else:
                    self.id = Task._id_counter

    def __str__(self):
        return f"ID: {self.id}\nTask:{self.title}\nPriority:{self.priority}\nState:{'Done' if self.state else 'Pending'}"

    # Additional methods

    def toggle_done(self) -> bool:
        self.state = not self.state
        return self.state

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "state": self.state,
            "priority": self.priority,
        }

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(
            data["title"],
            priority=data["priority"],
            state=data["state"] == "True",
        )
        task.id = int(data["id"])
        cls._id_counter = max(cls._id_counter, task.id + 1)
        return task

    # adding properties

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority: str):
        if priority in Task.priorities:
            self._priority = priority
        else:
            raise ValueError(f"Invalid priority. Choose from: {', '.join(Task.priorities)}.")


# Defining the TaskManager class
class TaskManager:
    def __init__(self, file="tasks.csv"):
        self.file = file
        self.tasks = self.load_tasks()

    # essential methods

    def load_tasks(self):
        if os.path.exists(self.file):
            with open(self.file, "r", newline="", encoding="utf-8") as File:
                reader = csv.DictReader(File)
                return [Task.from_dict(row) for row in reader]
        return []

    def write_tasks(self):
        with open(self.file, "w", newline="", encoding="utf-8") as File:
            fieldnames = ["id", "title", "state", "priority", ]
            writer = csv.DictWriter(File, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())

    # additional methods

    def add_task(self, task):
        self.tasks.append(task)
        self.write_tasks()

    def del_task(self, task):
        try:
            task = int(task)
            for _task in self.tasks:
                if _task.id == task:
                    self.tasks.remove(_task)
                    self.write_tasks()
                    return True
        except ValueError:
            for _task in self.tasks:
                if _task.title == task:
                    self.tasks.remove(_task)
                    self.write_tasks()
                    return True
        return False

    def list_tasks(self):
        for task in self.tasks:
            print("=" * 20)
            print(task)

    def toggle_done(self, task):
        try:
            task = int(task)
            for _task in self.tasks:
                if _task.id == task:
                    _task.toggle_done()
                    self.write_tasks()
                    return True
        except ValueError:
            for _task in self.tasks:
                if _task.title == task:
                    _task.toggle_done()
                    self.write_tasks()
                    return True
        return False

    def task(self, task):
        try:
            task = int(task)
            for _task in self.tasks:
                if _task.id == task:
                    print(_task)
                    return True
        except ValueError:
            for _task in self.tasks:
                if _task.title == task:
                    print(_task)
                    return True
        return False


# Define the main function
def main():
    if len(sys.argv) < 2:
        raise ValueError("Not enough data: file.py #mode #Input")
    mode = sys.argv[1]
    Input = sys.argv[2:]

    # Selecting the mode.
    match mode:
        case "add_task":  # adding task
            add_task(Input)
        case "toggle_done":  # marking a task done
            toggle_done(Input)
        case "del_task":  # deleting a task
            del_task(Input)
        case "list_tasks":  # printing all the tasks
            list_tasks()
        case "task":  # finding out the status of a specific task
            task(Input)
        case _:
            print("Invalid mode. Coose one: 'task', 'add_task', 'toggle_done', 'del_task', 'list_tasks'.")


# Defining all the Wrapper functions
def add_task(args):
    if not args:
        print("Please follow this structure: python file.py add_task <task_title> [priority]")
        return
    title = args[0]
    priority = args[1] if len(args) > 1 else Task.priorities[1]
    new_task = Task(title, priority)
    tm = TaskManager()
    tm.add_task(new_task)
    print("Task's been added successfully.")


def toggle_done(args):
    if len(args) != 1:
        print("Please follow this structure: python file.py toggle_done <task_title or task_id>")
        return
    tm = TaskManager()
    if tm.toggle_done(args[0]):
        print("Task has been toggled done.")
    else:
        print(f"No task found with ID {args[0]}.")


def del_task(args):
    if len(args) != 1:
        print("Please follow this structure: python file.py del_task <task_title or task_id>")
        return
    tm = TaskManager()
    if tm.del_task(args[0]):
        print("Task has been removed.")
    else:
        print(f"No task found with ID {args[0]}.")


def task(args):
    if len(args) != 1:
        print("Please follow this structure: python file.py task <task_title or task_id>")
        return
    tm = TaskManager()
    tm.task(args[0])


def list_tasks():
    tm = TaskManager()
    tm.list_tasks()


# The entry point
if __name__ == "__main__":
    main()
