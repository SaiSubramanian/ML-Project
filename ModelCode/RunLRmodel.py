from ModelCode.LRmodel import LinearRegressionModel as LRM
import pandas as pd


def trainModel():
    print("Working in RunLR")
    model = LRM()
    finalData = pd.read_csv('C:\\Users\\SubramanianR\\Downloads\\RFS_Account_Summary_modified\\RFS_Account_Summary_modified_till_18.csv')
    xTrain, xTest, yTrain, yTest = model.dataSplit(finalData)
    """x = pd.concat([xTrain, yTrain], ignore_index=True, sort=False)
    y = pd.concat([xTest, yTest], ignore_index=True, sort=False) """
    modelTrain = model.dataTrain(xTrain, yTrain)  
    # modelTest = model.dataTest(modelTrain, xTest)
    return finalData, modelTrain
