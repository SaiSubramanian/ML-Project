import pandas as pd
from CntryToGeo import getGeo
from GetParams import getParams
from LRmodel import LinearRegressionModel as LRM
from RunLRmodel import trainModel

dataset = pd.read_csv("C:\\Users\\SubramanianR\\Documents\\TestData3.csv")
print(dataset.shape)
print(dataset.head())

lrm = LRM()
dataset = dataset[dataset['IBM_STEP'] == 'Complete']
dataset = dataset[dataset['CNTRCT_TYPE_DESC'] == 'Production Contract']
dates = dataset['DATE']
step = dataset['IBM_STEP']
fd, model = trainModel()
dataset_new = dataset.groupby(
    ["CONTRACT_COUNTRY", "TXN_TYPE_DESC", "SECTOR",
     "PROPOSAL_PRICING_TERMS", "COMPLEXITY", "REQUEST TYPE"], as_index=False).sum()

for i in range(len(dataset_new['CONTRACT_COUNTRY'])):
    dataset_new.at[i, 'CONTRACT_COUNTRY'] = getGeo(dataset_new.at[i, 'CONTRACT_COUNTRY'])

dataset_new.rename(columns={"CONTRACT_COUNTRY": "CONTRACT_GEO"}, inplace=True)

dataset_new = dataset_new.groupby(
    ["CONTRACT_GEO", "TXN_TYPE_DESC", "SECTOR",
     "PROPOSAL_PRICING_TERMS", "COMPLEXITY", "REQUEST TYPE"], as_index=False).sum() 

# ONEHOT ENCODING BLOCK
enc = pd.get_dummies(dataset_new,
                     columns=['CONTRACT_GEO', 'REQUEST TYPE', 'COMPLEXITY', 'PROPOSAL_PRICING_TERMS',
                              'SECTOR', 'TXN_TYPE_DESC'])
print(enc.head())
print(enc.shape)

FinalData = pd.DataFrame(columns=getParams())
print(FinalData.columns)
actualWinCnt = enc['RFS_WIN_CNT']
enc = enc.drop(['RFS_WIN_CNT'], axis=1)
for i in list(FinalData.keys()):
    if i in enc.columns:
        FinalData[i] = enc[i].values
    else:
        FinalData[i] = [0 for n in range(len(enc))]

# FinalData = FinalData[(FinalData.iloc[i].values).count(1) == 6]
"""print(FinalData.index)
print(len(FinalData['CONTRACT_GEO_UKI']))
for i in range(len(FinalData['CONTRACT_GEO_UKI'])):
    if list(FinalData.iloc[i]).count(1) != 6:
        print(i, FinalData.iloc[i])
        FinalData = FinalData.drop(FinalData.index[i]) """

FinalData['RQST_RCVD_CNT'] = enc['RQST_RCVD_CNT'].values
print(FinalData.head())
FinalData.to_csv('C:\\Users\\SubramanianR\\Documents\\JNtest.csv', index=False)
FinalData['Predicted_WIN_CNT'] = lrm.dataTest(model, FinalData)
FinalData['Actual_WIN_CNT'] = actualWinCnt


for n in range(len(FinalData)):
    if FinalData.at[n, 'RQST_RCVD_CNT'] == 0:
        FinalData.at[n, 'Win%'] = "Can't predict.....Insufficient data" 
    elif (FinalData.at[n, 'Predicted_WIN_CNT'] / FinalData.at[n, 'RQST_RCVD_CNT']) > 1:
        FinalData.at[n, 'Win%'] = '100'
    else:
        FinalData.at[n, 'Win%'] = str(int(round((FinalData.at[n, 'Predicted_WIN_CNT'] / FinalData.at[n, 'RQST_RCVD_CNT']) * 100)))

FinalData['CURRENT_STEP'] = step
FinalData['DATE'] = dates
FinalData.to_csv('C:\\Users\\SubramanianR\\Documents\\TestNew4.csv', index=False)
