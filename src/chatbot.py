import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load configuration
with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

# Initialize the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(prompt):
    # Encode the input and generate a response
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.strip()
