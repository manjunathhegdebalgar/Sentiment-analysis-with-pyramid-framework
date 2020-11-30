# Sentiment-analysis-with-pyramid-framework
This is a sentiment analysis project that uses twitter data to classify reviews as positive and negative. The project uses Python pyramid framework as a front end where users can enter a new review and can get back the predicted along with the confidence of prediction.

Instructions to run the Project:
1. Download the project and name the folder with whatever name you want. [Here I use 'sentimentanalysis' as my project name]
2. Create a virtual environment in Python and activate it.
3. Move to the project directory i.e. cd parent_directory/sentimentanalysis and install the requirements with "pip install -r requirements.txt". The execution of 
   this command should get you all the dependencies required to run the project
4. Move one step above the directory i.e to the parent directory which contains the project(cd ..) and run "pip install -e sentimentanalysis". This will install 
   mysite package by running setup.py file in the project.
5. Move to the project folder and run "pserve development.ini"
6. You will get the link in which the app is being served and visiting the link will get you to a simple web page where you can type the review in the input box and   get the prediction
