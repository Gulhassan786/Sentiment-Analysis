import pandas as pd
import streamlit as st
import json
import pickle
import nltk
from nltk.corpus import stopwords
from streamlit_lottie import st_lottie
from PIL import Image

# Importing svm trained model and fited tfidf vectorizer
svm = pickle.load(open("pkl_files/svm.pkl","rb"))
tfidfvector = pickle.load(open("pkl_files/tfidf.pkl","rb"))

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

    if "review" in tfidf_predict_dataset.columns:

        tfidf_predict_data = tfidf_predict_dataset["review"]
        data.seek(0)
        data_to_show_user = pd.read_csv(data)

        nltk.download("stopwords")
        stop_words = [elements.lower() for elements in set(stopwords.words("english"))]

        data = tfidf_predict_data.str.lower()
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
        st.markdown(f"{pos} positive reviews and {neg} negative reviews")

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
    else:
        st.write("csv must contain review column")

# function for reading animation avaiable in jason format

def main():

    banner = Image.open("assets/chat.png")
    st.set_page_config(page_title="Sentiment Detection", page_icon=banner, )

    image = Image.open("assets/banner.jpg")
    st.image(image, width= 330)

     # css to hide main, footer and header given by streamlit default
    hide_st_menu = """
    <style>
    #MainMenu {visibility: hidden;}
    footer "{visibility: hidden;}
    header {visibility: hidden;}
    # .css-12oz5g7 {background-color:#e6e6ff}
    # .css-1t6ys2s {padding-left: 15rem}
    </style>
    """
    # code to apply above css in python
    st.markdown(hide_st_menu, unsafe_allow_html=True)

    st.header("Sentiment Analysis 🙂")
    
    # dropdown for the text input
    with st.expander("Analyze Text"):
    # taking text as input from the user
        txt = st.text_input("Write text here: ")
        # Checking if text is given the do preprocessing and predition and show it to the user
        if txt:
            # Method to preprocess the data
            txt_processing(txt)

    # Dropdown for the csv input so, user can upload csv 
    with st.expander("Analyze CSV: "):
        # Getting csv from the user and storing it in varaible so later will use it for prediction
        data = st.file_uploader("CSV must contain column review", type="csv")
        # checking if file is uploaded so, can procced to preprocessing and prediction
        if data:
            # Method to preprocess the data
            csv_preprocessing(data)
        
# Calling main function here to run our app
if __name__ == '__main__':
    main()
