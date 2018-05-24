import pandas as pd
import numpy as np
import globalparameter, csv, itertools
from sklearn import preprocessing
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

def KNN():
    user_profile = pd.read_csv(globalparameter.folderpath[1]+'/test1.csv')

    X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
                      'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
                      'normalized_work_year_past6']]  # use highest degree, six past work experience
    Y = user_profile['normalized_now_relevant_job']
    # np.unique(Y)   # out: array([0, 1, 2])

    # split test and train set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    # train logestic regression
    decision_tree_classifier = ()
    decision_tree_classifier.fit(X_train, Y_train)
    Y_score = decision_tree_classifier.decision_function(X_test_std)

    # predict
    prediction = decision_tree_classifier.predict((X_test_std))
    prepro = decision_tree_classifier.predict_proba(X_test_std)
    acc = decision_tree_classifier.score(X_test_std, Y_test)
    avg_precesion = average_precision_score(Y_test,Y_score)

    print('prediction is : {}'.format(prediction))
    print('-------')
    print('Logestic regression')
    print('prepro is : {}'.format(prepro))
    print('acc is predict proba is {}'.format(acc))
    print('average precision and recall is {}'.format(avg_precesion))

    #plot the diagram
    precision, recall, _ = precision_recall_curve(Y_test,Y_score)

    # plt.step(recall, precision, color='blue', alpha=0.2,where='post')
    plt.plot(recall,precision,label = 'KNN')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(avg_precesion))
    plt.savefig(globalparameter.folderpath[1] + '/diagram_logestic_regression_p-r_' + globalparameter.jobtitle_path_list[1] + '-extract' + '.png')