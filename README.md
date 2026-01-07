Hugging Space Servisine İstek atmak için oluşturuldu
İnaktiviteden dolayı ilk istek 15 20 sn zaman alabilir.

OST /predict endpoint’i var.
Hugging Face modelini kullanarak texti analiz eder ve duygu sonucunu döner. Render üzerinden kaldırıldı

Anladığım kadarıylee gradio Spaces arka planda kendi özel protokolüyle çalışıyor ve doğrudan HTTP REST istekleri kabul etmiyor.
bundan ötürü Spaces’i Python gradio_client üzerinden çağıran bir ara servis yazdım.

https://pythonservice-2.onrender.com/predict den istekleri kabul eder

istek atılan servis:

import gradio as gr
from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = analyzer(text)[0]
    label = result['label']
    return label  # "POSITIVE", "NEGATIVE", "NEUTRAL"

iface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")
iface.launch()

