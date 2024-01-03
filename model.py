from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summary_pipline(ARTICLE: str):
    return summarizer(ARTICLE, max_length=500, min_length=100, do_sample=False)