import pandas as pd
from pandas import DataFrame
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


#reading data
kingcnt = pd.read_csv("data/King_County_House_prices_dataset.csv")

df_kingcnt = DataFrame(kingcnt,columns=['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15']) 


#dealing with missing values
df_kingcnt.fillna({'waterfront':0, 'view':0}, inplace=True)


#transforming data
df_kingcnt['price_log'] = np.log(df_kingcnt['price'])
df_kingcnt['sqft_lot_log'] = np.log(df_kingcnt['sqft_lot'])
df_kingcnt['sqft_lot15_log'] = np.log(df_kingcnt['sqft_lot15'])


#splitting data
print("-----  Splitting the data in train and test ----")
train, test = train_test_split(df_kingcnt, test_size=0.33, random_state=42)


#cleaning training data
train = train[train.bedrooms != 33]
train = train[train.sqft_living < 12000]
train = train[train.sqft_lot < 1100000]
train = train[train.sqft_above < 9000]
train = train[train.sqft_lot15 < 500000]


#feature engineering
X_train = df_kingcnt[['bedrooms','bathrooms','sqft_living','sqft_lot_log','waterfront','view','grade','sqft_above','sqft_living15','sqft_lot15_log']]
y_train = df_kingcnt['price_log']
X_test = df_kingcnt[['bedrooms','bathrooms','sqft_living','sqft_lot_log','waterfront','view','grade','sqft_above','sqft_living15','sqft_lot15_log']]
y_test = df_kingcnt['price_log']


#adding the constant
X_train = sm.add_constant(X_train) # adding a constant
X_test = sm.add_constant(X_test) # adding a constant


#training the model
print("-----  Training the model ----")
model = sm.OLS(y_train, X_train).fit()
print_model = model.summary()


#predictions to check the model
print("-----  Evaluating the model ----")
predictions = model.predict(X_train)
err_train = np.sqrt(mean_squared_error(y_train, predictions))
predictions_test = model.predict(X_test)
err_test = np.sqrt(mean_squared_error(y_test, predictions_test))


print(print_model)
print ("-------------")
print (f"RMSE on train data: {err_train}")
print (f"RMSE on test data: {err_test}")
