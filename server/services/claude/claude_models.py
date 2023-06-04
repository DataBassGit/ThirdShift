class SelectModel():
    def __init__(self, model_choice="claude-v1"):
        """
        Given a model choice, returns the corresponding model name.
        If the choice is not valid, return a string describing available models.
        :param model_choice: string, the user's model choice
        :return: string, the selected model name or a string describing available models
        """
        # Define a dictionary of valid models with their names as keys
        self.models={
            "claude-v1": "claude-v1",
            "claude-v1-100k": "claude-v1-100k",
            "claude-instant-v1": "claude-instant-v1",
            "claude-instant-v1-100k": "claude-instant-v1-100k",
            "claude-v1.3": "claude-v1.3",
            "claude-v1.3-100k": "claude-v1.3-100k",
            "claude-v1.2": "claude-v1.2",
            "claude-v1.0": "claude-v1.0",
            "claude-instant-v1.1": "claude-instant-v1.1",
            "claude-instant-v1.1-100k": "claude-instant-v1.1-100k",
            "claude-instant-v1.0": "claude-instant-v1.0"
        }
        self.model_choice = model_choice
        self.model_name = self.chose_model()


    def chose_model(self):
        # Get the model name corresponding to the user's choice
        chosen_model = self.models.get(self.model_choice, None)
        # If the model choice is invalid, return a string describing available models
        if chosen_model is None:
            return """
            - Claude v1:
            Anthropic's largest model, ideal for a wide range of more complex tasks.
            model, particularly for complex tasks. However, it is much less expensive and blazing fast. We believe that this model provides more than adequate performance on a range of tasks including text classification, summarization, and lightweight chat applications, as well as search result summarization
            - Claude v1 100k:
            An enhanced version of claude-v1 with a 100,000 token (roughly 75,000 word) context window. Ideal for summarizing, analyzing, and querying long documents and conversations for nuanced understanding of complex topics and relationships across very long spans of text.
            - Claude instant v1:
            A smaller model with far lower latency, sampling at roughly 40 words/sec! Its output quality is somewhat lower than the latest claude-v1 model, particularly for complex tasks. However, it is much less expensive and blazing fast. We believe that this model provides more than adequate performance on a range of tasks including text classification, summarization, and lightweight chat applications, as well as search result summarization.
            - Claude-instant-v1-100k:
            An enhanced version of claude-instant-v1 with a 100,000 token context window that retains its performance. Well-suited for high throughput use cases needing both speed and additional context, allowing deeper understanding from extended conversations and documents.
            - Claude v1.3:
            Compared to claude-v1.2, it's more robust against red-team inputs, better at precise instruction-following, better at code, and better and non-English dialogue and writing.
            - Claude v1.3 100k:
            An enhanced version of claude-v1.3 with a 100,000 token (roughly 75,000 word) context window.
            - Claude v1.2:
            An improved version of claude-v1. It is slightly improved at general helpfulness, instruction following, coding, and other tasks. It is also considerably better with non-English languages. This model also has the ability to role play (in harmless ways) more consistently, and it defaults to writing somewhat longer and more thorough responses.
            - Claude v1.0:
            An earlier version of claude-v1.
            - Claude instant v1.1:
            Our latest version of claude-instant-v1. It is better than claude-instant-v1.0 at a wide variety of tasks including writing, coding, and instruction following. It performs better on academic benchmarks, including math, reading comprehension, and coding tests. It is also more robust against red-teaming inputs.
            - Claude instant v1.1 100k:
            An enhanced version of claude-instant-v1.1 with a 100,000 token context window that retains its lightning fast 40 word/sec performance.
            - Claude instant v1.0:
            An earlier version of claude-instant-v1.
            """
        return chosen_model
