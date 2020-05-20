import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
df=pd.read_csv("D:\dataset\Iris.csv")
df.shape
df.head(30)
df.describe()
df.groupby('class').size()
df.plot(kind='box', subplots= True, layout=(2,2), sharex= False, sharey= False)
plt.show()
scatter_matrix(df)
plt.show()
array= df.values
X= array[:,0:4]
Y= array[:,4]
validation_size=0.20
seed = 6
X_train, X_test, Y_train, Y_test= model_selection.train_test_split(X,Y, test_size = validation_size, random_state=seed)
seed=6
scoring='accuracy'
models=[]
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
results=[]
names=[]
for name, model in models:
    kfold= model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model,X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)" %(name, cv_results.mean(), cv_results.std())
    print(msg)
    
