import os
import sys
sys.path.join(os.path.dirname(os.path.dirname("./")))
from services.claude.claude_options import SelectOptions

import unittest

class TestSelectOptions(unittest.TestCase):
    def test_construct_call(self):
        options = SelectOptions(
            api_key="my_api_key",
            prompt="Hello, world!",
            model="claude-v1",
            max_tokens=1000,
            stop_sequence=["\n\nHuman:","\n\nAssistant:"],
            stream=True,
            temperature=1.5,
            top_k=5,
            top_p=0.9,
            metadata={"user_id": 123}
        )

        expected_request = {
            "url": "https://api.anthropic.com/v1/complete",
            "method": "POST",
            "headers":{
                "x-api-key": "my_api_key",
                "content-type": "application/json",
            },
            "prompt": "Hello, world!",
            "model": "claude-v1",
            "max_tokens_to_sample": 1000,
            "stop_sequences": ["\n\nHuman:","\n\nAssistant:"],
            "stream": True,
            "temperature": 1.5,
            "top_k": 5,
            "top_p": 0.9,
            "metadata": {"user_id": 123}
        }

        self.assertEqual(options.construct_call(), expected_request)


if __name__ == '__main__':
    unittest.main()
