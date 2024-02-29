# Sentiment-Analysis 🙂
<br>
<h1> About Model 🤖</h1>
Had created the sentiment analysis model on <bold> Movie reviews dataset</bold>. Trained 5 machine learning models on the same dataset 😑
<ul> 
  <li> Random Forest </li>
   <li> Naive Bayes </li>
   <li> Logistic Regression </li>
   <li> Decision Tree </li>
   <li> Support Vector Machine (SVM) </li>
</ul>


SVM gives good accuracy than other models so I preferred to go with it. <b>Accuracy of the model is 0.89 </b>.
<h3>Steps for Model training 🦾</h3>
<ol> 
  <li> Read the data using pandas, Removed any number or special symbols by applying regex on data</li>
   <li>Removed stop words (common words in English) from the reviews for better accuracy </li>
   <li>Sotred those strings of data into list</li>
   <li> Created Bag Of Words (BOW) using TFIDF Vectorizer so can feed it to the model for training </li>
   <li>Created Model, selected its hyperparameters, and passed it BOW as well as y data set for training </li>
   <li>After training we used x test data to test the model performance</li>
   <li>Used different methods such as cofusion matrix and accuracy score to check model performance</li>
</ol>

<br>
<h2> Repo Structure 🗄️ </h2>

<ol> 
  <li> You will see the <b> assets folder</b> it contains images that, had used in the web app as I had deployed the model on web</li>
  <li>You will find the dataset and <b>.ipynb </b> file in the <b>python_model_code folder</b> which there is complete code from data preprocessing and how I trained the model</li>
  <li>You will find a few files with <b> .pkl </b> extension in <b> pkl_files folder </b> might be you thinking why do I have those files, what is there needed, I trained the model, and want to create web app but I have to write whole code for training and test in that web app it will be not a good approach as I had trained model so, I had export trained model using python pickle library. with those files, I can use my trained model for prediction directly and also it reduces the code-end training time. </li>
  <li> <b> main.py </b> is file for web app. I had written  web app code in that file using streamlit library from Python </li>
  <li> <b>Requirements.txt</b> file contains libraries that I need to install on the server when I deploy my web app on the server so, my model can be accessed and used easily throughout the world </li>
</ol>

<br>
<h3> Web App Link 🌐</h3>
<button her> </button>
<a href="https://sentiment-detection.streamlit.app">Checkout Model by yourself </a>

<h2>I am on</h2>

<ul>

<li> <a href="https://github.com/gulhassan786" >Github</a></li>
 <li> <a href="https://www.linkedin.com/in/gul-hassan-7b188b202/">LinkedIn</a></li>
  <li> <a href="https://www.kaggle.com/hassangul">Kaggle</a></li>
 <li> <a href="https://medium.com/@gulhassanh49">Medium</a></li> 
 
 </ul>
