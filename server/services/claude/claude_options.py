class SelectOptions():
    def __init__(self, api_key=None, prompt=None, model="claude-v1", max_tokens_to_sample=8000, stop_sequence=None, stream=True, temperature=1, top_k=1, top_p=1, metadata=None):
        """
        Initialize SelectOptions with the given parameters.
        :param api_key: string, the API key to authenticate with Anthropic's API
        :param prompt: string, the input prompt for the model
        :param model: string, the name of the model to use
        :param max_tokens_to_sample: int, the maximum number of tokens to output
        :param stop_sequence: list of strings, the stop sequences to stop generating output at
        :param stream: bool, whether to stream the output or return it all at once
        :param temperature: float, the temperature of the sampling distribution
        :param top_k: int, the number of top tokens to consider for sampling
        :param top_p: float, the cumulative probability threshold for top-k sampling
        :param metadata: dict, additional metadata to include in the request
        """
        if stop_sequence is None:
            stop_sequence = ["\n\nHuman:","\n\nAssistant:"]
        self.api_key = api_key
        self.prompt = prompt
        self.model = model
        self.max_tokens_to_sample = max_tokens_to_sample
        self.stop_sequence = stop_sequence
        self.stream = stream
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
        self.metadata = metadata

    def construct_call(self):
        """
        Construct the request to send to Anthropic's API.
        :return: dict, the request to send to Anthropic's API
        """
        return {
            "url": "https://api.anthropic.com/v1/complete",
            "method": "POST",
            "headers": {
                "x-api-key": self.api_key,
                "content-type": "application/json",
            },
            "prompt": self.prompt,
            "model": self.model,
            "max_tokens_to_sample": self.max_tokens_to_sample,
            "stop_sequences": self.stop_sequence,
            "stream": self.stream,
            "temperature": self.temperature,
            "top_k": self.top_k,
            "top_p": self.top_p,
            "metadata": self.metadata,
        }

if __name__=="__main__":
    options = SelectOptions(
            api_key=None,
            prompt=None,
            model="claude-v1",
            max_tokens_to_sample=8000,
            stop_sequence=["\n\nHuman:","\n\nAssistant:"],
            stream=True,
            temperature=1,
            top_k=1,
            top_p=1,
            metadata=None
            )
    print(options.construct_call())