import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinearRegressionModel:

    def dataSplit(self, FinalData):
        X = FinalData.drop(['RFS_WIN_CNT'], axis=1)
        y = FinalData['RFS_WIN_CNT']
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=100)
        return X_train, X_test, y_train, y_test

    def dataTrain(self, X_train, y_train):
        lm = LinearRegression()
        lm.fit(X_train, y_train)
        return lm

    def dataTest(self, lm, X_test):
        yPredict = lm.predict(X_test)
        val = []
        for i in yPredict:
            if i < 0:
                # val.append(round(abs(i)))
                val.append(0)
            else:
                val.append(round(i))
        return val
