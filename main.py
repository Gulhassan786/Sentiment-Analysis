import pandas as pd
import streamlit as st
import json
import pickle
import nltk
from nltk.corpus import stopwords
from streamlit_lottie import st_lottie

svm = pickle.load(open("svm.pkl","rb"))
tfidfvector = pickle.load(open("tfidf.pkl","rb"))

def txt_processing (txt):
            
        lst_data = txt.lower()

        nltk.download("stopwords")
        stop_words = [elements.lower() for elements in set(stopwords.words("english"))]
       
        lst_data = lst_data.split(sep=" ")

        lst_data = list([val for val in lst_data if val.isalpha()])

        def remove_stop (x):
            return ",".join([words for words in x if words not in stop_words])
        
        data =  remove_stop(lst_data)
        data = ["".join(data)]

        tfidf_predict_data = tfidfvector.transform(data)
        prediction = svm.predict(tfidf_predict_data)

        if prediction[-1] == 1:
            st.write("Review is: Positive")
        else:
            st.write("Review is: Negative",)

def csv_preprocessing (data):
    tfidf_predict_dataset = pd.read_csv(data)

    data.seek(0)
    data_to_show_user = pd.read_csv(data)

    nltk.download("stopwords")
    stop_words = [elements.lower() for elements in set(stopwords.words("english"))]

    data = tfidf_predict_dataset["review"].str.lower()
    data.replace("[^a-zA-Z]"," ", regex=True, inplace=True)


    def remove_stop (x):
        return ",".join([words for words in str(x).split() if words not in stop_words])

    data = data.apply(lambda x: remove_stop(x))

    predict_array = []
    for row in range(0, len(data.index)):
            predict_array.append("".join(x for x in data.iloc[row] ))
    tfidf_predict_data = tfidfvector.transform(predict_array)

    predictions = svm.predict(tfidf_predict_data)

    pos = 0
    neg = 0
    if len(predictions)>2:
        
        for i in predictions:
            if i == 1:
                pos +=1
            else:
                neg +=1
    st.write(f"{pos} positive reviews and {neg} negative reviews")

        # Inserting new column to the users data and will give it back to the user
    @st.cache
    def convert_df(data, predictions):

        data["label"] = 2
        for i in range(0,len(predictions)):
            data["label"][i] = predictions[i]

        return data

    data_to_show_user = convert_df(data_to_show_user, predictions)
    st.write(data_to_show_user.head(10))
    data_to_show_user = data_to_show_user.to_csv().encode('utf-8')
        
    st.download_button(
            label="Download data as CSV",
            data = data_to_show_user,
            file_name="sentiment.csv",
            mime="csv",
        )

def load_lottiefile(filepath: str):

    with open(filepath, "r", encoding="utf8") as f:
        return json.load(f)

if __name__ == '__main__':

    st.set_page_config(page_title="Sentiment Detection", page_icon="🤗")
    # ui_width = st_js.st_javascript("window.innerWidth")
    lottie_coding = load_lottiefile("assets/robotrun.json") 
    lottie_coding2 = load_lottiefile("assets/dancerobot.json") 
    st_lottie(lottie_coding2, speed=1, reverse=False, loop=True, quality="high", # medium ; high height= 200,
        width= 200,
        key="animation",)

    hide_st_menu = """
    <style>
    #MainMenu {visibility: hidden;}
    footer "{visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st_menu, unsafe_allow_html=True)
    st.header("Sentiment Analysis 🙂")
        
    # dropdown for the text input
    with st.expander("Analyze Text"):
    # taking text as input from the user
        txt = st.text_input("Write text here: ")
        # Checking if text is given the do preprocessing and predition and show it to the user
        if txt:
            txt_processing(txt)

    # Dropdown for the csv input so, user can upload csv 
    with st.expander("Analyze CSV: "):
        # Getting csv from the user and storing it in varaible so later will use it for prediction
        data = st.file_uploader("Upload file must conatin review column", type="csv")
        # checking if file is uploaded so, can procced to preprocessing and prediction
        if data:
            csv_preprocessing(data)
        
