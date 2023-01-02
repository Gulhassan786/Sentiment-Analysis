# Sentiment-Analysis 🙂
<br>
<h1> About Model </h1>
Had created the sentiment analysis model on <bold> Movie reviews dataset</bold>. Trained 4 machine learning models on same dataset such as 
<ul> 
  <li> Random Forest </li>
   <li> Naive Bayes </li>
   <li> Logistic Regression </li>
   <li> Decision Tree </li>
   <li> Support Vector Machine (SVM) </li>
</ul>


SVM give good accuraccy then other models so i prefered to go with it. <b>Accuracy of the model is 0.89 </b>.
<h3>Steps for Model training</h3>
<ol> 
  <li>Readed the data using pandas, Removed the any number or special symbols by applying regex on data</li>
   <li>Removed stop words (common words in english) from the reviews for batter accuracy </li>
   <li>Sotred those strings of data into list</li>
   <li> Created Bag Of Words (BOW) using TFIDF Vectorizer so can feed it to the model for training </li>
   <li>Created Model, selected its hyper parameters and passed it BOW as well as y data set for traing</li>
   <li>After training we used x test data to test the model performance</li>
   <li>Used different methods such as cofusion matrix and accuracy score to check model performance</li>
</ol>

<br>
<h2> Folder Structure </h2>

<ol> 
  <li>  you will see the <b> assests folder</b> it contain images that i had used in web app as had deployed model on web</li>
  <li>You will find dataset and <b>.ipynb </b> file in which there is complete code of from data preprocessing and how i trained the model</li>
  <li>You will find few files with <b> .pkl </b> extension might be you are thinking why i had those file, whats there need so, I trained model and want to created web app but i have to write whole code for training and test in the that web app it will be not good approach as i had trained model so, i had export trained model using python pickle library. with those files i can use my trained model for prediction directly and also it reduces the code end training time. </li>
  <li> <b> main.py </b> is file for web app. I had written  web app code in that file using streamlit library from python </li>
  <li> <b>Requirements.txt</b> file contain libraries that i need to install on server when i will deploy my web app on the server so, my model can be accessed and used easily through out the world </li>
</ol>

<br>
<h3> Web App Link</h3>
<button her> </button>
<a href="https://sentiment-detection.streamlit.app" style={
            background-color: black;
<!--             border: 2px solid black;
            color: green;
            padding: 5px 10px;
            text-align: center;
            display: inline-block;
            font-size: 20px;
            margin: 10px 30px;
            cursor: pointer;
            text-decoration:none; -->
        }>Checkout Model by yourself </a>

