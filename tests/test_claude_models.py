import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname("./")))
from services.claude.claude_models import SelectModel

class TestClaudeModels():
    def __init__(self)->None:
        pass

    def test_select_model(self):
        expected_output = "claude-v1"
        model = SelectModel(model_choice=expected_output)
        self.assertEqual(model.model_name, expected_output)

if __name__ == '__main__':
    unittest.main()