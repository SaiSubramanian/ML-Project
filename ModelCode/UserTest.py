from ModelCode.LRmodel import LinearRegressionModel as LRM
import pandas as pd
import operator as op

def predictProb(fd, lm, data):
    lrm = LRM()
    testData = {}
    print("Working in Testmode")
    output = 0
    # fd = fd.drop("Unnamed: 0", axis=1)
    for x in list(fd.keys()):
        if x != 'RQST_RCVD_CNT' and x != 'RFS_WIN_CNT':
            if x not in data:
                testData[x] = 0
            else:
                testData[x] = 1
    rqst_cnt, win_cnt = 0, 0
    tempfd = fd.drop(['RQST_RCVD_CNT', 'RFS_WIN_CNT'], axis=1)
    print(fd.columns)
    print(fd.shape)

    for i in range(len(tempfd)):
        tempfdList = []
        for j in (tempfd.values)[i]:
            tempfdList.append(j)
        if op.eq(list(testData.values()), tempfdList):
            rqst_cnt += fd['RQST_RCVD_CNT'][i]
            win_cnt += fd['RFS_WIN_CNT'][i]
    testData = pd.DataFrame([testData])
    testData.insert(0, 'RQST_RCVD_CNT', rqst_cnt, True)
    print(testData.shape)
    testData['Predicted_WIN_CNT'] = lrm.dataTest(lm, testData)
    testData['Actual_WIN_CNT'] = win_cnt
    print(testData)
    if testData.at[0, 'RQST_RCVD_CNT'] == 0:
        output = "Can't predict.....\n Insufficient data"
        return output
    elif (testData.at[0, 'Predicted_WIN_CNT'] / testData.at[0, 'RQST_RCVD_CNT']) > 1:
        output = 100.0
    else:
        output = round((testData.at[0, 'Predicted_WIN_CNT'] / testData.at[0, 'RQST_RCVD_CNT']) * 100)
    
    print('Output', output)
    return (str(int(output)) + '%')
