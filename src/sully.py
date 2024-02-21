import torch
from ctransformers import AutoModelForCausalLM
from transformers import pipeline
from random import randint


class dummySully():
    llm_pipeline = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    def prompt(self, prompt):
        messages = [
            {
                "role": "system",
                "content": "Answer with short and concise answers. With no more explanations than necessary.",
            },
            {"role": "user", "content": prompt},
        ]
        prompt = self.llm_pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.llm_pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

        return outputs[0]["generated_text"].split("<|assistant|>\n")[1]

class Sully():
    prev = ""

    def __init__(self):
        torch.cuda.empty_cache()
        self.llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-Chat-GGUF", model_file="llama-2-7b-chat.Q5_K_S.gguf", model_type="llama", gpu_layers=750, context_length=4096)

    def prompt(self, prompt):
        prompt_template = f"""
        [INST] 
        <<SYS>>
        Answer with short and concise answers. With no more explanations than necessary. The previous answer was: {self.prev}
        <</SYS>>
        {prompt}
        [/INST]"""

        answer = self.llm(prompt_template, top_p=0.9, top_k=50, temperature=0.7, max_new_tokens=768, seed=randint(0, 1000))
        self.prev = answer

        return answer
