# firstname_analysis_api

## Introduction:
This API takes firstname and dob as input and generates a summary with nickname, prediction, and zodiac sign.

## Getting Started:
1. Clone or download the project first
2. Install the following dependencies using 'pip':<br/>
  ```pip install Flask```<br/>
  ```pip install Flask-RESTful```<br/>
  ```pip install mysql```<br/>
  ```pip install mysql-connector-python```<br/>
  ```pip install mysqlclient```<br/>
3. Navigate to the folder containing flask_api.py and run it using ```python flask_api.py```
4. Open http://127.0.0.1:5000/ in the browser/postman and use the following URL to generate the output<br/>
  http://127.0.0.1:5000/nameanalysis?firstname={firstname}&dob={dd/mm}

## About
1. This application is a REST API with a backend MySql database to store user_logs and prediction data
2. It randomly generates predictions based on the users firstname and dob(date of birth)
3. Also as mentioned in the requirements if the same name and dob is given as input, a consistent output would be generated
4. Adding to this to make the outout more unique, a nick name generater is embedded in the response

## Sample input and output: [This API is hosted on Heroku and can be accessed with the below link]
Input : https://firstnameanalysis.herokuapp.com/nameanalysis?firstname=steve&dob=1/1
Output : "Hi steve,Your zodiac sign is: Capricorn and your nickname is: st342 Your prediction is :You are torn between the future and the past and must find ways to bring them together. The best way, of course, is to learn from what has gone before and make sure you don?t make the same mistakes all over again."

## Any of the following scenarios would lead to a validation failure:
1. Empty firstname
2. Empty dob
3. Empty firstname and dob
4. Integer input in the place of firstname[String]
5. Dob format [dd/mm] dd range is 1 to 30 and mm range is 1 to 12

## Live Demo:
https://firstnameanalysis.herokuapp.com/nameanalysis?firstname={firstname}&dob={dd/mm}

Sample : https://firstnameanalysis.herokuapp.com/nameanalysis?firstname=steve&dob=1/1
