import torch
from transformers import pipeline


class Sully:
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16,
                    device_map="auto")


    def prompt(self, message):
        # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
        messages = [
            {
                "role": "system",
                "content": "You are a friendly chatbot who responds with short answers",
            },
            {"role": "user", "content": message},
        ]
        prompt = self.pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
        return outputs[0]["generated_text"].split("\n<|assistant|>\n")[1]


