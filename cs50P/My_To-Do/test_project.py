# test_task_manager.py
import os
import tempfile
import pytest
from project import Task, TaskManager

# This fixture sets up a TaskManager with a temporary CSV file.
@pytest.fixture
def temp_manager():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()                       # Only need the file name
    manager = TaskManager(file=temp_file.name)
    yield manager                           # Provide the fixture value to the tests
    os.unlink(temp_file.name)               # Clean up, remove the file after test

def test_add_task(temp_manager):
    # Test that adding a task increases the task count.
    initial_count = len(temp_manager.tasks)
    new_task = Task("Test Add", "Secondary")
    temp_manager.add_task(new_task)

    # Reinitialize the TaskManager to simulate persisting to file.
    new_manager = TaskManager(file=temp_manager.file)
    assert len(new_manager.tasks) == initial_count + 1
    assert new_manager.tasks[-1].title == "Test Add"

def test_toggle_done(temp_manager):
    # Test that toggling a task's status works.
    new_task = Task("Test Toggle", "Primary")
    temp_manager.add_task(new_task)

    result = temp_manager.toggle_done(str(new_task.id))
    new_manager = TaskManager(file=temp_manager.file)
    toggled_task = next((t for t in new_manager.tasks if t.id == new_task.id), None)

    assert result is True
    assert toggled_task is not None
    assert toggled_task.state is True

def test_del_task(temp_manager):
    # Test that deleting a task works.
    new_task = Task("Test Delete", "Primary")
    temp_manager.add_task(new_task)
    initial_count = len(temp_manager.tasks)

    result = temp_manager.del_task(str(new_task.id))
    new_manager = TaskManager(file=temp_manager.file)

    assert result is True
    assert len(new_manager.tasks) == initial_count - 1
    assert not any(t.id == new_task.id for t in new_manager.tasks)
