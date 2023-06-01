import os
import sys
sys.path.join(os.path.dirname(os.path.dirname('/')))

class PromptTemplate():
    def __init__(self, user_input=None):
        self.userQuestion = user_input

    def prompt_tempalte(self):
        self.prompt = f"\n\nHuman: {self.userQuestion}\n\nAssistant:"
        return self.prompt

