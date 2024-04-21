import torch
import transformers

from huggingface_hub import login 
login(token = "")

model_id = "meta-llama/Llama-2-7B-chat-hf"

# Set up the chat generation pipeline with desired parameters
pipeline = transformers.pipeline(
    "text2text-generation", 
    model=model_id, 
    device_map="auto",
    model_kwargs={"torch_dtype": torch.bfloat16}, 
    max_length=500,  # Adjust the max_length parameter to set the maximum length of generated responses
    min_length=100,   # Optionally set a minimum length for responses
    temperature=0.5, # Control the randomness of sampling (lower values are more deterministic)
)

def generate_response(prompt):
    # Generate text using the pipeline with the provided prompt
    generated_text = pipeline(prompt)
    return generated_text
