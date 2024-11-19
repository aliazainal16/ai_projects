import chatgpt
import prompts

prompt = prompts.twitter_thread_generator_prompt.format(topic="digital marketing")

response = chatgpt.llm_generate_text(prompt, "gpt-4o-mini")

print(response)

