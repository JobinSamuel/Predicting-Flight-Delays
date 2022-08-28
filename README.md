# Predicting-Flight-Delays
There are many reasons which contribute to flight delays like Poor Weather Conditions, Security Issues, Technical Issues with the aircraft, Waiting for connecting passengers, Airport congestion, Late Arrival of Aircraft. Etc.
Predicting delays using various types of Regression like Gradient boosting Regression, Decision Tree Regression, Logistic Regression, Bayesian ridge, Random Forest Regression. 
Collecting historical data to train the model. Cleaning the historical using various data cleansing technique and imputing missing data and normalizing data if required. And extracting features like Departure Delay, Airline, Flight Number, Destination Airport, Origin Airport, Day of the Week, Taxi out, Day. 
Splitting the data into three parts where 60% of the data will be considered as training data 20% will be considered as validation data and the remaining 20% data will be considered as test data.
Machine learning algorithms were applied, progressively and successively to predict flight arrival & delay. We built five models.
We saw for each evaluation metric like Mean squared error(MSE), Mean absolute error(MAE), Explained Variance, Median absolute error, and R2 scores are considered and the values of each model are taken and compared.
The model which gives the best value in maximum metrics is selected for prediction.
Then visualizing the metrics with respect to the models shows the results. 
In Departure Delay and Arrival Delay , Random Forest Regressor was observed as the best model with Mean Squared Error and Mean Absolute Error, which are the minimum value found in these respective metrics. 
In the rest of the metrics, the value of the error of Random Forest Regressor although is not minimum but still gives a low value comparatively. In maximum metrics, we found out that Random Forest Regressor gives us the best value and thus should be the model selected. 
Finally deploying the model using DJANGO Framework.
![image](https://user-images.githubusercontent.com/86288918/187066267-e96c27e7-9518-45f9-8669-0840b1113807.png)
