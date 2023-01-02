# Sentiment-Analysis
<br>
<h1> About Model </h1>
Had created the sentiment analysis model on <bold> Movie reviews data</bold>. Trained 4 machine learning models such as 
<ul> 
  <li> Random Forest </li>
   <li> Naive Bayes </li>
   <li> Logistic Regression </li>
   <li> Decision Tree </li>
   <li> Support Vector Machine (SVM) </li>
</ul>


SVM give good accuraccy then other models so i prefered to go with it. Accuracy of the model is 0.89.
<br>
<h2> Folder Structure </h2>

<ol> 
   <li>  you will see the assests folder it contain images that i had used in web app as had deployed model on web</li>
   <li>You will find dataset and .ipynb file in which there is complete code of from data preprocessing to model training </li>
   <li>You will find few files with .pkl extension might be you are thinking why i had those file, whats there need so, I trained model and want to created web app but i have to write whole code for training and test in the that web app it will be not good approach as i had trained model so, i had export trained model using python pickle library. with those files i can use my trained model for prediction directly and also it reduces the code end training time. </li>
   <li> main.py is file for web app. I had written  web app code in that file using streamlit library from python </li>
   <li> Requirements.txt file contain libraries that i need to install on server when i will deploy my web app on the server so, my model can be accessed and used easily through out the world </li>
</ol>


