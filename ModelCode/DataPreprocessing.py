import pandas as pd
from CntryToGeo import getGeo

FinalData = pd.DataFrame()
dataset = pd.read_csv('C:\\Users\\SubramanianR\\Downloads\\RFS_Account_Summary_2010_19_regression.csv')
print(dataset.shape)
dataset_new = dataset[dataset['CNTRCT_TYPE_DESC'] == 'Production Contract']
dataset_new = dataset_new.drop(
    ["TCV_CATALOG_ORDERS_YTD", "TCV_NON_PRICED_YTD", "TCV_CTLG_PRICE_AMT", "UNIQUE_ID",  "RQST_COUNTRY",
     "PROC_TITLE", "TXN_TYPE_CD", "CNTRCT_TYPE_DESC", "CONTRACT_NUMBER", "CNTRCT_DIM_UID", "Unnamed: 0"], axis=1)
print(dataset_new.shape)    

df = pd.read_csv('C:\\Users\\SubramanianR\\Documents\\TestData1.csv')
df = df.drop(['IBM_STEP', 'DATE'], axis=1)
df = df[df['CNTRCT_TYPE_DESC'] == 'Production Contract']
dataset_new = pd.concat([dataset_new, df], ignore_index=True, sort=False) 

df = pd.read_csv('C:\\Users\\SubramanianR\\Documents\\TestData2.csv')
df = df.drop(['IBM_STEP', 'DATE'], axis=1)
df = df[df['CNTRCT_TYPE_DESC'] == 'Production Contract']
dataset_new = pd.concat([dataset_new, df], ignore_index=True, sort=False) 

dataset_new = dataset_new.groupby(
    ["CONTRACT_COUNTRY", "CONTRACT_NAME", "TXN_TYPE_DESC", "SECTOR",
     "PROPOSAL_PRICING_TERM", "COMPLEXITY", "REQUEST TYPE"], as_index=False).sum()

for i in range(len(dataset_new['CONTRACT_COUNTRY'])):
    dataset_new.at[i, 'CONTRACT_COUNTRY'] = getGeo(dataset_new.at[i, 'CONTRACT_COUNTRY'])

dataset_new.rename(columns={"CONTRACT_COUNTRY": "CONTRACT_GEO"}, inplace=True)

dataset_new = dataset_new.groupby(
    ["CONTRACT_GEO", "CONTRACT_NAME", "TXN_TYPE_DESC", "SECTOR",
     "PROPOSAL_PRICING_TERM", "COMPLEXITY", "REQUEST TYPE"], as_index=False).sum() 

# ONEHOT ENCODING BLOCK
enc = pd.get_dummies(dataset_new,
                     columns=['CONTRACT_GEO', 'REQUEST TYPE', 'COMPLEXITY', 'PROPOSAL_PRICING_TERM',
                              'SECTOR', 'TXN_TYPE_DESC'])

dataset_new = dataset_new.drop(
    ['CONTRACT_NAME', 'CONTRACT_GEO', 'REQUEST TYPE', 'COMPLEXITY', 'PROPOSAL_PRICING_TERM',
     'SECTOR', 'TXN_TYPE_DESC'], axis=1)
enc = enc.drop(['CONTRACT_NAME', 'RQST_RCVD_CNT', 'RFS_WIN_CNT'], axis=1)

FinalData = pd.concat([dataset_new, enc], axis=1)
print(FinalData.shape)

CheckNull = FinalData.drop(['RQST_RCVD_CNT', 'RFS_WIN_CNT'], axis=1)
for i in range(len(CheckNull['CONTRACT_GEO_UKI'])):
    if list(CheckNull.iloc[i].values).count(1) != 6:
        FinalData = FinalData.drop(FinalData.iloc[i], axis=1) 

print(FinalData.head())
print(FinalData.shape)
FinalData.to_csv('C:\\Users\\SubramanianR\\Documents\\RFS_Account_Summary_2010_19_regression.csv', index=False)
