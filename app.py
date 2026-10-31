import gradio as gr
from summarizer import summarize

gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(label="Enter a URL"),
    outputs=gr.Markdown(label="Summary"),
    title="Website Summarizer",
    description="Enter a URL to get a concise summary of the website's main content.",
    theme="default"
).launch(share=True)


