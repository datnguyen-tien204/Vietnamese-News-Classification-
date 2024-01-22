import streamlit as st
import tensorflow as tf
from keras.models import load_model
import pandas as pd
import pickle
import numpy as np
from modulePreprocessing import preprocessing
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

st.header("Category Classification for Vietnamese Newspaper")
def show_gif(text):
    if text=="Bạn đọc":
        st.markdown("![Alt Text](https://media.giphy.com/media/FOh0sXN9C0I0Neq2Fy/giphy.gif)")
    if text=="Bất động sản":
        st.markdown("![Alt Text](https://media.giphy.com/media/nMm87SjyNIdbH3Mzrf/giphy.gif)")
    if text=="Công nghệ":
        st.markdown("![Alt Text](https://media.giphy.com/media/doXBzUFJRxpaUbuaqz/giphy.gif)")
    if text=="Công đoàn":
        st.markdown("![Alt Text](https://media.giphy.com/media/51YplJK6nbtwf17tAu/giphy.gif)")
    if text=="Diễn đàn":
        st.markdown("![Alt Text](https://media.giphy.com/media/ADD4w6XgqLBJohQdBK/giphy.gif)")
    if text=="Gia đình - Hôn nhân":
        st.markdown("![Alt Text](https://media.giphy.com/media/xT5LMXR7iA0mSSxOBG/giphy.gif)")
    if text=="Giáo dục":
        st.markdown("![Alt Text](https://media.giphy.com/media/KDYB0cH4HW8xc3VIAx/giphy.gif)")
    if text=="Kinh doanh":
        st.markdown("![Alt Text](https://media.giphy.com/media/LZ2WRdQu8udNPSZxbg/giphy.gif)")
    if text=="Lao Động & Đời sống":
        st.markdown("![Alt Text](https://media.giphy.com/media/ThrM4jEi2lBxd7X2yz/giphy.gif)")
    if text=="Lao Động cuối tuần":
        st.markdown("![Alt Text](https://media.giphy.com/media/wogeWaRfUjlMv6T6we/giphy.gif)")
    if text=="Lưu trữ":
        st.markdown("![Alt Text](https://media.giphy.com/media/xUNd9KuqkEuWwgZ9u0/giphy.gif)")
    if text=="Media":
        st.markdown("![Alt Text](https://media.giphy.com/media/26tk0jALFpsXmAF8c/giphy.gif)")
    if text=="Pháp luật":
        st.markdown("![Alt Text](https://media.giphy.com/media/p9WGfmQMEENR9zRmCO/giphy.gif)")
    if text=="Phóng sự":
        st.markdown("![Alt Text](https://media.giphy.com/media/n2IPMYMthV0m4/giphy.gif)")
    if text=="Sức khoẻ":
        st.markdown("![Alt Text](https://media.giphy.com/media/1eExMzjHzTrmEJjMsW/giphy.gif)")
    if text=="Sự kiện Bình luận":
        st.markdown("![Alt Text](https://media.giphy.com/media/NNMTmcrK2wRmrj0MuO/giphy.gif)")
    if text=="Thông tin tiện ích":
        st.markdown("![Alt Text](https://media.giphy.com/media/8FxaYF4jKVytcumRS8/giphy.gif)")
    if text=="Thế giới":
        st.markdown("![Alt Text](https://media.giphy.com/media/l1KVcrdl7rJpFnY2s/giphy.gif)")
    if text=="Thể thao":
        st.markdown("![Alt Text](https://media.giphy.com/media/dWrDicEgHO52f9k8Du/giphy.gif)")
    if text=="Thời sự":
        st.markdown("![Alt Text](https://media.giphy.com/media/aIBBzADjpNqhi/giphy.gif)")
    if text=="Tin hoạt động":
        st.markdown("![Alt Text](https://media.giphy.com/media/9tSHlTxblykjoYluPj/giphy.gif)")
    if text=="Tin tức việc làm":
        st.markdown("![Alt Text](https://media.giphy.com/media/qLVwr3jkgf4MBPxuyM/giphy.gif)")
    if text=="Tấm Lòng Vàng":
        st.markdown("![Alt Text](https://media.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif)")
    if text=="Văn hóa - Giải trí":
        st.markdown("![Alt Text](https://media.giphy.com/media/QtPcBUZrdH66YI6bZp/giphy.gif)")
    if text=="Xe +":
        st.markdown("![Alt Text](https://media.giphy.com/media/i1QcGGAog9Z6bt2KCx/giphy.gif)")
    if text=="Xã hội'":
        st.markdown("![Alt Text](https://media.giphy.com/media/fo37FYKqdsudaGWIog/giphy.gif)")



def load_model(dict_label,tokenizer,model):
    with open(f'{dict_label}','rb') as f:
        dict_label = pickle.load(f)
    with open(f'{tokenizer}','rb') as f:
        tok = pickle.load(f)
    model = tf.keras.models.load_model(f"{model}",compile=False)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return dict_label,tok,model
dct_lb=r"E:\NLP\Vietnamese-Text-Classification-master\Model NLP\BiGRU\results_2\dict_label.pkl"
tokenizer=r"E:\NLP\Vietnamese-Text-Classification-master\Model NLP\BiGRU\results_2\tokenize_text.pkl"
model_path=r"E:\NLP\Vietnamese-Text-Classification-master\Model NLP\BiGRU\results_2\wandb\run-20231201_154325-f8e475vx\files\model-best.h5"

dict_label,tok,model=load_model(dct_lb,tokenizer,model_path)


input_str = st.text_area("Enter something text")

button_pressed = st.button("Confirm")
if button_pressed:
    try:
        if(input_str==""):
            st.warning("Text input must be different null")
        else:
            df = preprocessing(input_str)
            test_sequences = tok.texts_to_sequences(df)
            max_len = 2000
            test_sequences_matrix = pad_sequences(test_sequences, maxlen=max_len, padding='post')
            y_predict = model.predict(test_sequences_matrix)

            i = 0
            st.text("Category Predicted")
            text_show=dict_label[str(np.argmax(y_predict[i]))]
            st.success(text_show)
            show_gif(text_show)
        #print(f"Giá trị dự đoán: {dict_label[str(np.argmax(y_predict[i]))]}")
    except:
        pass
