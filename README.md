# 📱 SMS Spam Detector

A simple NLP model that classifies SMS messages as **Spam** or **Not Spam (Ham)**.  
This project fine-tunes **DistilBERT** on the popular SMS Spam dataset and deploys it using **Gradio**.

---

## 🚀 Demo
Try the live demo here 👉 [Hugging Face Space](https://huggingface.co/spaces/itserphan/sms-spam-detector-demo)

---

## 📊 Model Performance
The model was trained on the [SMS Spam Collection dataset](https://huggingface.co/datasets/sms_spam) and achieved:

- **Accuracy:** ~97%  
- **Precision:** ~99%  
- **Recall:** ~95%  
- **F1-score:** ~96%

---

## 🧪 Example Usage
You can test the model with examples like:

```text
Spam: "Congratulations! You have won a free ticket to Bahamas. Reply WIN to claim now!"
Ham: "Hey, are we still meeting for coffee tomorrow?"
