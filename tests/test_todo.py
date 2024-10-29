import sys
import os

# Include the src directory in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from todo import add_task, remove_task, view_tasks

class TestTodoFunctions(unittest.TestCase):

    def setUp(self):
        """Initialize a shared task list for tests."""
        self.task_list = []

    def test_add_task(self):
        """Test adding a task to task list."""
        add_task(self.task_list, "Buy milk")
        self.assertIn("Buy milk", self.task_list)
    
    def test_remove_task(self):
        """Test removing a task from task list."""
        self.task_list.append("Read book")
        remove_task(self.task_list, "Read book")
        self.assertNotIn("Read book", self.task_list)

    def test_remove_nonexistent_task(self):
        """Test removing a task that doesn't exist in task list."""
        remove_task(self.task_list, "Walk the dog")
        self.assertEqual(len(self.task_list), 0)  # Ensure no change in empty list

    def test_view_tasks(self):
        """Test viewing tasks returns formatted string."""
        self.task_list.extend(["Buy milk", "Read book"])
        output = view_tasks(self.task_list)
        expected_output = "1. Buy milk\n2. Read book"
        self.assertEqual(output, expected_output, "The output should list all tasks.")

    def test_view_tasks_empty(self):
        """Test viewing tasks on an empty task list."""
        output = view_tasks(self.task_list)
        self.assertEqual(output, "No tasks available.")

if __name__ == '__main__':
    unittest.main()