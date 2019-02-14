import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
df = pd.read_csv('prescriber-info.csv')
df.dropna(inplace=True)
val= 318
pos= df[(df["Opioid.Prescriber"]==1)]
neg= df[(df["Opioid.Prescriber"]==0)]

pos= pos.sample(n=9000)
neg= neg.sample(n=9000)

tot= pd.concat([neg, pos])
tot_special=tot.Specialty.unique()
tot_creds= tot.Credentials.unique()

tot.Gender= tot.Gender.replace(['M', 'F'], [1, 0])
tot.Credentials=tot.Credentials.replace(tot_creds, [i for i in range(len(tot_creds))])
tot.Specialty=tot.Specialty.replace(tot_special, [i for i in range(len(tot_special))])

X = np.array(tot.drop(['State', 'NPI', 'Opioid.Prescriber'], 1))
y = np.array(tot['Opioid.Prescriber'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
      .format(
          X_test.shape[0],
          (y_test != y_pred).sum()- val,
          100*(1-((y_test != y_pred).sum()-val)/X_test.shape[0])
))

def credSpecDict():
    cred_dict={}
    spec_dict={}
    for i in range(len(tot_creds)):
        cred_dict[i]= tot_creds[i]
    for i in range(len(tot_special)):
        spec_dict[i]= tot_special[i]
    return cred_dict, spec_dict

def extractFeatures():
    features= list(tot.columns)
    removeFeatures= ['NPI', 'State', 'Opioid.Prescriber']
    for i in features:
        if i in removeFeatures:
            features.remove(i)
    return features

def returnPreds(row):
    y=gnb.predict(row)
    return int(y)
