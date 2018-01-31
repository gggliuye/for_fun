import pandas as pd

temp = pd.read_csv('data.csv')
temp1 = temp['p_change']
temp['price_2'] = temp1
temp['price_3'] = temp1
temp['price_4'] = temp1
temp['price_5'] = temp1
temp['price_6'] = temp1
temp['pred'] = temp1


i = 1
while i<= 1080 :
  temp.at[i,'pred'] = temp1[i-1] 
  temp.at[i,'price_2'] = temp.at[i+2,'close']
  temp.at[i,'price_3'] = temp.at[i+3,'close']
  temp.at[i,'price_4'] = temp.at[i+4,'close']
  temp.at[i,'price_5'] = temp.at[i+5,'close']
  temp.at[i,'price_6'] = temp.at[i+6,'close']
  i = i + 1

temp.at[0,'price_2'] = temp.at[2,'close']
temp.at[0,'price_3'] = temp.at[3,'close']
temp.at[0,'price_4'] = temp.at[4,'close']
temp.at[0,'price_5'] = temp.at[5,'close']
temp.at[0,'price_6'] = temp.at[6,'close']


temp.at[0,'pred'] = 0; 
test = temp.iloc[1:201,:]
pred = temp.iloc[0:51,:]
train = temp.iloc[201:1085,:]

test.to_csv('data_test.csv')
train.to_csv('data_train.csv')
pred.to_csv('data_pred.csv')