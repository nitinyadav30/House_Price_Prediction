import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
#data = pd.read_csv("Housing.csv")
#df = pd.DataFrame(data)
class data_import:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path)
        self.modal = LinearRegression()
        #print(self.df)
    def preprocessing(self):
        try:
            #print(self.df.info())
            #print(self.df.isnull().sum())
            self.df["airconditioning"] = self.df["airconditioning"].replace({"yes": 1, "no": 0})
            self.df["mainroad"] = self.df["mainroad"].replace({"yes": 1, "no": 0})
            self.df["guestroom"] = self.df["guestroom"].replace({"yes": 1, "no": 0})
            self.df["basement"] = self.df["basement"].replace({"yes": 1, "no": 0})
            self.df["hotwaterheating"] = self.df["hotwaterheating"].replace({"yes": 1, "no": 0})
            a = pd.get_dummies(self.df["furnishingstatus"], dtype=np.int64)
            self.df = pd.concat([self.df, a], axis=1)
            self.df = self.df.drop(["furnishingstatus"], axis=1)
            #print(self.df)
            #print(self.df.info())
            x_train, x_test, y_train, y_test = self.data_split()
            self.training_modal(x_train, x_test, y_train, y_test)
            self.test_modal(x_test, y_test)
            self.IQR_Calculation(self.df)
            #print(f"x_train shape: {x_train.shape} y_train shape {y_train.shape}")
            #print(f"x_test shape: {x_test.shape} y_test shape {y_test.shape}")
        except Exception as e:
            print(f"Error in preprocessing-{e.__str__()}")
    def data_split(self):
        try:
            x = self.df.iloc[:,1:]
            y = self.df.iloc[:,0]
            #print(x)
            #print(y)
            x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.10, random_state=42)
            return x_train, x_test, y_train, y_test
        except Exception as e:
            print(f"Error in data_split-{e.__str__()}")

    def training_modal(self, x_train, x_test, y_train, y_test):
        try:
            self.modal.fit(x_train, y_train)
            y_train_pred = self.modal.predict(x_train)
            print(f" The training accuracy is: {r2_score(y_train, y_train_pred)}")
        except Exception as e:
            print(f"Error in Training Modal {e.__str__()}")
    def test_modal(self, x_test, y_test):
        try:
            y_test_pred = self.modal.predict(x_test)
            print(f"The Test Accuracy of the Modal is: {r2_score(y_test, y_test_pred)}")

        except Exception as e:
            print(f"The error is in Test Modal {e.__str__()}")

    def test_modal(self, x_test, y_test):
        try:
            y_test_pred = self.modal.predict(x_test)
            print(f"The Test Accuracy of the Modal is: {r2_score(y_test, y_test_pred)}")
        except Exception as e:
            print(f"The error is in Test Modal: {e._str_()}")

    def IQR_Calculation(self, df):
        try:
            Q1 = self.df["area"].quantile(0.25)
            Q3 = self.df["area"].quantile(0.75)
            IQR = Q3 - Q1
            print(f"The IQR value is {IQR}")
        except Exception as e:
            print(f"The error is in IQR: {e.__str__()}")

if __name__ == '__main__':
    obj = data_import("D:/Internship Jul-Aug 2023/Project/Housing.csv")
    obj.preprocessing()



#modal = LinearRegression()
#modal.fit(x_train, y_train)
#modal.fit(x_test, y_test)
#y_train_pred = modal.predict((x_train))
#print(f"The modal training accuracy is {r2_score(y_train, y_train_pred)}")
#y_test_pred = modal.predict((x_test))
#print(f"The modal test accuracy is {r2_score(y_test, y_test_pred)}")

#modal2 = Lasso(alpha=0.2)
#modal2.fit(x_train, y_train)
#y2_predict = modal2.predict(x_train)
#print(r2_score(y_train,y2_predict))