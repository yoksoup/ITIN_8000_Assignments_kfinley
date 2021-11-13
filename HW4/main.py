"""
Kyle Finley
Homework 4
11/12/2021

Output:
---KNN---
-list percent accuracy per each K value
-Graphs out a 80% training and 20% testing graph
-list percent accuracy per each K value
-Then Graphs 5 more times with random values between 1%:83%
(set because if it is too high it does not have enough data to test.)

---Gaussian---
-lists out accuracy 80:20 sample run
-lists out accuracy for 5 random value runs

---MLP---
-lists out accuracy 80:20 sample run
-lists out accuracy for 5 random value runs
(random values go up to 30%-70% for test/training
since it gets errors above that

Credits:
# https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
-they walk through a lot of the steps and explain how they work
-their git-repo is broken though, so just had to type through the code

"""
# -----import section-----
# sklearn iris data
from sklearn.datasets import load_iris
# for random values
import random
# imports the KNeighborsClassifier class from sklearn
from sklearn.neighbors import KNeighborsClassifier
# imports metrics model to check the accuracy
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import math
# for GaussianNB
from sklearn.naive_bayes import GaussianNB
# for MLP
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

# -----initialized variables-----
# how many times to do random values for training/testing
# keep under 19 if charts are on or pycharm gets angry
random_runtimes = 5 # produces charts
random_runtimes_gauss = 5
random_runtimes_MLP = 5

# limits set for graph axis
lower_glimit = .7
higher_glimit = 1

# -----Debug Displays-----
# it will show if = 1 and not if = 0
show_percents_per_k = 1 # percent lists
show_charts = 1 # graphs
KN_distance = 0 # turns on distance weight
show_sample_size = 0 # testing sample sizes
show_gsample_size = 0 # for gaussian sample sizes
show_gaussian = 1 # displays the gaussian percents
# -----------------------

# sets the k_range to be 1 to 25
k_range = range(1,26)

# load iris data into iris variable and set type
iris = load_iris()
type(iris)

# store the iris data and target values as X and y
X = iris.data
y = iris.target

# output statements for testing
"""
print(iris.feature_names)
print(iris.data)
print(iris.target)
print(iris.target_names)
print(iris.data.shape)
"""

# -----First, Training 80:20 Testing, Graph-----
# splits the training and test sets 80:20
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=4)

# output statements for testing
"""
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
"""

# creates the objects for scores and score_list
scores = {}
scores_list = []

# Produces the accuracy scores for every k in k range, 1 to 25 by default
for k in k_range:
    # if distance bool is turned on does distance weight
    if KN_distance == 0:
        knn = KNeighborsClassifier(n_neighbors=k,)
    else:
        knn = KNeighborsClassifier(n_neighbors=k, weights='distance')
    # fits the nearest neighbors from the data set
    knn.fit(X_train, y_train)
    # predicts the class label
    y_pred=knn.predict(X_test)
    # captures the accuracy into a list
    scores[k] = metrics.accuracy_score(y_test,y_pred)
    # appends scores_list
    scores_list.append(metrics.accuracy_score(y_test,y_pred))

# prints out the scores
if show_percents_per_k == 1:
    print("K1-25 80:20 Values")
    print_list = [f'{i*100:.1f}%' for i in scores_list]
    print(print_list)

# set to fig 1 for first graph
fig = 1

# plot figure with number and size of window
plt.figure(fig, figsize=(8, 6))
# set and plot title
plt.title("Training 80:20 Testing split")
plt.plot(k_range,scores_list)
# graph limits, .7 to 1 is default
plt.ylim([lower_glimit,higher_glimit])
# set the x and y labels for graph
plt.xlabel("Value of K for KNN")
plt.ylabel("Testing Accuracy")


# -----Next 5, Training Random:Random Testing, Graphs-----
# splits the training and test sets randomly
# runs random_runtimes amount of times, default 5.
for i in range(random_runtimes):
    # up the figure count for new window
    fig += 1
    # sets sample size to random value between 1 and 83
    # 85 or greater produces errors since not enough testing
    sam_size = random.randint(1,83)/100

    # output statements for testing
    if show_sample_size == 1:
        print("sample size:", sam_size)

    # splits the training and test sets randomly
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=sam_size,random_state=4)

    # output statements for testing
    """print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)"""

    # creates the objects for scores and score_list
    scores = {}
    scores_list = []

    # Produces the accuracy scores for every k in k range, 1 to 25 by default
    # appends it to a scores_list
    for k in k_range:
        # if distance bool is turned on does distance weight
        if KN_distance == 0:
            knn = KNeighborsClassifier(n_neighbors=k, )
        else:
            knn = KNeighborsClassifier(n_neighbors=k, weights='distance')
        # fits the nearest neighbors from the data set
        knn.fit(X_train, y_train)
        # predicts the class label
        y_pred=knn.predict(X_test)
        # captures the accuracy into a list
        scores[k] = metrics.accuracy_score(y_test,y_pred)
        # appends scores_list
        scores_list.append(metrics.accuracy_score(y_test,y_pred))

    # prints out the scores
    if show_percents_per_k == 1:
        print("K1-25 random-split Values:", fig)
        print_list = [f'{i * 100:.1f}%' for i in scores_list]
        print(print_list)

    # plot figure with number and size of window
    plt.figure(fig, figsize=(8, 6))
    # set and plot title
    plt.plot(k_range,scores_list)
    plot_title = "Training " + str(math.trunc((1-sam_size)*100)) + ":" + str(math.trunc(sam_size *100)) + " Testing split"
    plt.title(plot_title)
    # graph limits, .7 to 1 is default
    plt.ylim([.7,1.0])
    # set the x and y labels for graph
    plt.xlabel("Value of K for KNN")
    plt.ylabel("Testing Accuracy")

# displays created plots
if show_charts == 1:
    plt.show()

print("----------------------------------")
# -----Gaussian NB-----

# load iris data into iris variable and set type
X, y = load_iris(return_X_y=True)

# splits the training and test data 80:20
sam_size = .2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=sam_size, random_state=0)

# makes gaussian nb object
gnb = GaussianNB()

# uses the gaussianNB meathod to train and predict data points
y_pred = gnb.fit(X_train, y_train).predict(X_test)

# prints out the percent accuracy
if show_gaussian == 1:
    percent = ("{:.1%}".format(((X_test.shape[0] - (y_test != y_pred).sum())) / X_test.shape[0]) * 100)[0:3]
    print("Gaussian ", ((1 - sam_size) * 100), ":", sam_size * 100, " - Percent accuracy =", percent)


# -----Next 5 Gaussian, Training Random:Random Testing, Graphs-----
# splits the training and test sets randomly
# runs random_runtimes amount of times, default 5.
for i in range(random_runtimes_gauss):

    # sets sample size to random value between 1 and 84
    # 85 or greater produces errors since not enough testing
    sam_size = random.randint(1,98)/100

    # output statements for testing
    if show_gsample_size == 1:
        print("sample size:", sam_size)

    # splits the training and test sets randomly
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=sam_size,random_state=4)

    # uses the gaussianNB meathod to train and predict data points
    y_pred = gnb.fit(X_train, y_train).predict(X_test)

    # prints out the percent accuracy
    if show_gaussian == 1:
        percent = ("{:.1%}".format(((X_test.shape[0] - (y_test != y_pred).sum()))/ X_test.shape[0])*100)[0:3]
        print("Gaussian ", ((1-sam_size)*100),":", sam_size*100,"- Percent accuracy =", percent )

print("----------------------------------")
# -----Multilayer-----
# sets the number of samples and the random state
X, y = make_classification(n_samples=30, random_state=1)
# splits the training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)
# sets the number of iterations
clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)

# calculates the percent accuracy
acc = clf.score(X_test, y_test)
print("MLP 80 : 20 accuracy: ", acc*100, "%")

for i in range(random_runtimes_MLP):
    # gets a random number for sample size
    sam_size = random.randint(5,99)
    X, y = make_classification(n_samples=sam_size, random_state=1)
    # splits the training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)
    # sets the number of iterations
    clf = MLPClassifier(random_state=1, max_iter=1000).fit(X_train, y_train)

    # calculates the percent accuracy
    acc = clf.score(X_test, y_test)
    print("MLP ", (1-(sam_size/150))*100, ":", (sam_size/150)*100, " accuracy: ", acc * 100, "%")
