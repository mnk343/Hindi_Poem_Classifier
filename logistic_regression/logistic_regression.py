# 
# 
# Code to predict the author name and the poem era given on the testing data
# based on the training data.
# The Model used here is Logistic Regression.
# 
# 

import pickle
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
import numpy as np


# Used to load the btf vectors 
with open("train_data_btf","rb") as f:
    train_data = pickle.load(f)

# Lists created for training data
train_data_list = []
list_poem_era = []
list_poem_author = []

# Store the author names and poem eras in the training data lists
for element in train_data:
	author_name = element[0]
	poem_era = element[3]
	list_poem_author.append(author_name)
	list_poem_era.append(poem_era)
	poem_vector = element[5]
	train_data_list.append(poem_vector)

# Converting lists into numpy arrays
train_data_vectors = np.array(train_data_list)
np_array_poem_era = np.array(list_poem_era)
np_array_poem_author = np.array(list_poem_author)

# test data loaded
with open("test_data_btf","rb") as f:
    test_data = pickle.load(f)

# Lists created for storing test data
test_data_list = []
list_correct_poem_era = []
list_correct_poem_author = []

# Store the correct author names and poem eras in the testing data lists
poem_index = 0 
for element in test_data:
	correct_author_name = element[0]
	correct_poem_era = element[3]
	correct_poem_vector = element[5]

	list_correct_poem_era.append(correct_poem_era)
	list_correct_poem_author.append(correct_author_name)
	test_data_list.append(correct_poem_vector)

# Converting test data lists to numpy arrays
test_data_vectors = np.array(test_data_list)
np_array_correct_poem_era = np.array(list_correct_poem_era)
np_array_correct_poem_author = np.array(list_correct_poem_author)

print("numpy array creation done")

# Fitting the logistic regression model using sklearn library

# Values of C, to be passed as a parameter
tuned_parameters = [{'C': [10**-4, 10**-2, 10**0, 10**2, 10**4]}]

# L2 REGULARISATION

# GridSearchCV Implementation

# max iterations set to be 1000
model1 = GridSearchCV(LogisticRegression(penalty='l2',max_iter=1000),tuned_parameters, scoring = 'accuracy', cv=3 ,n_jobs=-1,pre_dispatch=2)
model1.fit(train_data_vectors,np_array_poem_era)

print("L2 Regularisation\n\nGridSearchCV Implementation\n\n For Era Prediction")

print("Model with best parameters :\n",model1.best_estimator_)
print("Accuracy of the model : ",model1.score(test_data_vectors, np_array_correct_poem_era))

# prints the best value of C used while training the model
optimal_C = model1.best_estimator_.C
print("The optimal value of C(1/lambda) is : ",optimal_C)

model2 = GridSearchCV(LogisticRegression(penalty='l2',max_iter=1000),tuned_parameters, scoring = 'accuracy', cv=3, n_jobs=-1,pre_dispatch=2)
model2.fit(train_data_vectors,np_array_poem_author)

print(" For Author Prediction")

print("Model with best parameters :\n",model2.best_estimator_)
print("Accuracy of the model : ",model2.score(test_data_vectors, np_array_correct_poem_author))

# prints the best value of C used while training the model
optimal_C = model2.best_estimator_.C
print("The optimal value of C(1/lambda) is : ",optimal_C)

# RandomizedSearchCV Implementation

# Create regularization hyperparameter distribution using uniform distribution
C = uniform(loc=0, scale=10)

# Create hyperparameter options
hyperparameters = dict(C=C)

model3 = RandomizedSearchCV(LogisticRegression(penalty='l2',max_iter=1000),hyperparameters, scoring = 'accuracy', cv=3, n_jobs=-1,pre_dispatch=2)
model3.fit(train_data_vectors,np_array_poem_era)

print("L2 Regularisation\n\nRandomizedSearchCV Implementation\n\n For Era Prediction")

print("Model with best parameters :\n",model3.best_estimator_)
print("Accuracy of the model : ",model3.score(test_data_vectors, np_array_correct_poem_era))

# prints the best value of C used while training the model
optimal_C = model3.best_estimator_.C
print("The optimal value of C(1/lambda) is : ",optimal_C)

model4 = RandomizedSearchCV(LogisticRegression(penalty='l2',max_iter=1000),hyperparameters, scoring = 'accuracy', cv=3, n_jobs=-1,pre_dispatch=2)
model4.fit(train_data_vectors,np_array_poem_author)

print(" For Author Prediction")

print("Model with best parameters :\n",model4.best_estimator_)
print("Accuracy of the model : ",model4.score(test_data_vectors, np_array_correct_poem_author))

# prints the best value of C used while training the model
optimal_C = model4.best_estimator_.C
print("The optimal value of C(1/lambda) is : ",optimal_C)

