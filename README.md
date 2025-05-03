# Qwen3-0.6bReason
llamacpp server and qwen3 textual chat interface with reasoning options


Local LLM run from [HF repo](https://hf-mirror.com/Qwen/Qwen3-0.6B). Using [Bartowski quantized Q8 version from here](https://hf-mirror.com/bartowski/Qwen_Qwen3-0.6B-GGUF)


### Requirements
```
pip install rich openai
```


### Reasoning flags
Qwen API and Transformers tokenizers chat template have a dedicated flag to activate the reasoning.

with llamaCPP-server this is achieved with the soft tags at the end of the prompt

here extract from official HF repo

```
    # First input (without /think or /no_think tags, thinking mode is enabled by default)
    user_input_1 = "How many r's in strawberries?"
    print(f"User: {user_input_1}")
    response_1 = chatbot.generate_response(user_input_1)
    print(f"Bot: {response_1}")
    print("----------------------")

    # Second input with /no_think
    user_input_2 = "Then, how many r's in blueberries? /no_think"
    print(f"User: {user_input_2}")
    response_2 = chatbot.generate_response(user_input_2)
    print(f"Bot: {response_2}") 
    print("----------------------")

    # Third input with /think
    user_input_3 = "Really? /think"
    print(f"User: {user_input_3}")
    response_3 = chatbot.generate_response(user_input_3)
    print(f"Bot: {response_3}")

```
