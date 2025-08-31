import gradio as gr
from transformers import pipeline

# Load pipeline from your HF Hub repo
classifier = pipeline("text-classification", model="itserphan/sms-spam-detector")

def classify_sms(text):
    result = classifier(text)[0]
    label = result['label']
    score = round(result['score'], 3)
    return f"Prediction: {label} (confidence: {score})"

demo = gr.Interface(
    fn=classify_sms,
    inputs=gr.Textbox(lines=2, placeholder="Type your SMS message here..."),
    outputs="text",
    title="📩 SMS Spam Detector",
    description="Detects whether an SMS is spam or not using DistilBERT."
)

if __name__ == "__main__":
    demo.launch()