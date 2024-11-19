twitter_thread_generator_prompt = """Imagine you are a social media guru.
Create a 10-tweet thread about [{topic}].
The thread should be tailored for maximum virality and include hashtags and emoticons.
Each tweet must not exceed 280 characters."""

blog_bullet_summary_prompt = """\
In the next input, I will provide a text that needs summarizing 
into bullet points.
You will be given a maximum and a minimum number of bullet points
to use for the summary.
The language of the provided text will dictate the language of the summary.
For instance, if the text is in German, the summary should also be in German.
This applies to all languages. When summarizing,
keep in mind two important factors: "perplexity" and "burstiness."
Perplexity refers to the complexity of the text. Separately,
burstiness compares the variations in sentences.
Humans typically write with high burstiness, for example,
using a mix of longer or more complex sentences alongside shorter ones.
AI-generated sentences tend to be more uniform. Therefore,
when creating the summary,
ensure it exhibits a good amount of both perplexity and burstiness.
Maximum: [{MaxPoints}], Minimum: [{MinPoints}], Text: {InputText}"""