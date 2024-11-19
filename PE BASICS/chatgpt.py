import openai

# Set your OpenAI API key
openai.api_key = "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"
client = openai.OpenAI()

def llm_generate_text(prompt, model):
    return openai_generate(prompt, model)

def openai_generate(user_prompt, selected_model):
    completion = client.chat.completions.create(
        model=selected_model,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content