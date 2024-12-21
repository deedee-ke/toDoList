import sys
import os
import tempfile
import json

# Include the src directory in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from todo import add_task, remove_task, view_tasks, save_tasks, load_tasks, show_help

class TestTodoFunctions(unittest.TestCase):

    def setUp(self):
        """Initialize a shared task list for tests."""
        self.task_list = []
        # Create a temporary file for testing save/load
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_filename = self.temp_file.name

    def tearDown(self):
        """Clean up temporary files after tests."""
        os.unlink(self.temp_filename)

    def test_add_task(self):
        """Test adding a task to task list."""
        result = add_task(self.task_list, "Buy milk")
        self.assertIn("Buy milk", self.task_list)
        self.assertEqual(result, "Task 'Buy milk' added.")
    
    def test_remove_task(self):
        """Test removing a task from task list."""
        self.task_list.append("Read book")
        result = remove_task(self.task_list, "Read book")
        self.assertNotIn("Read book", self.task_list)
        self.assertEqual(result, "Task 'Read book' removed.")

    def test_remove_nonexistent_task(self):
        """Test removing a task that doesn't exist in task list."""
        result = remove_task(self.task_list, "Walk the dog")
        self.assertEqual(len(self.task_list), 0)
        self.assertEqual(result, "Task 'Walk the dog' not found in the list.")

    def test_view_tasks(self):
        """Test viewing tasks returns formatted string."""
        self.task_list.extend(["Buy milk", "Read book"])
        output = view_tasks(self.task_list)
        expected_output = "1. Buy milk\n2. Read book"
        self.assertEqual(output, expected_output)

    def test_view_tasks_empty(self):
        """Test viewing tasks on an empty task list."""
        output = view_tasks(self.task_list)
        self.assertEqual(output, "No tasks available.")

    def test_save_tasks(self):
        """Test saving tasks to a file."""
        self.task_list.extend(["Buy milk", "Read book"])
        save_tasks(self.task_list, self.temp_filename)
        with open(self.temp_filename, 'r') as file:
            saved_tasks = json.load(file)
        self.assertEqual(saved_tasks, self.task_list)

    def test_load_tasks_existing_file(self):
        """Test loading tasks from an existing file."""
        original_tasks = ["Buy milk", "Read book"]
        with open(self.temp_filename, 'w') as file:
            json.dump(original_tasks, file)
        loaded_tasks = load_tasks(self.temp_filename)
        self.assertEqual(loaded_tasks, original_tasks)

    def test_load_tasks_nonexistent_file(self):
        """Test loading tasks from a non-existent file."""
        nonexistent_file = "nonexistent.json"
        loaded_tasks = load_tasks(nonexistent_file)
        self.assertEqual(loaded_tasks, [])

    def test_show_help(self):
        """Test that show_help function exists and runs without error."""
        try:
            show_help()
        except Exception as e:
            self.fail(f"show_help() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()