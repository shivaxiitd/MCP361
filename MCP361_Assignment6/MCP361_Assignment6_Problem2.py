#Assignment 6
#Problem 2
#Siddharth Dixit
#2018ME20727

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

from scipy.stats import norm

n = 10000

# a = 0.2 & b = 0.3
# ab =[a, b]
ab = [0.2, 0.3]

#mean 0 and standard deviation 0.5
#msd = [mean, standard deviation]
msd = [0, 0.5]

X = np.linspace(1,5000,n)
s = np.random.normal(msd[0], msd[1], n)
y = []

x = 0
while x < n:
    y.append(ab[0]+ab[1]*X[x]+s[x])
    x = x + 1
    

x_train,x_test,y_train,y_test=train_test_split(X.reshape(-1, 1),y,test_size=0.2)

regression = LinearRegression().fit(x_train, y_train)
print("Regression Score =",regression.score(x_test,y_test))
intercept = regression.intercept_
slope = regression.coef_


y_pred = []
for xi in x_test:
    y_pred.append(regression.predict(xi.reshape(-1, 1))[0])


residual_error = []

i = 0
while i < len(y_test):
    residual_error.append(y_test[i] - y_pred[i])
    i = i + 1

X_axis = np.arange(len(x_test))
plt.bar(X_axis, residual_error)
plt.xlabel("X values")
plt.ylabel("Residual error values")
plt.title("Residual error histogram")
plt.cla()
mean, std = norm.fit(residual_error)
print("Mean =",mean)
print("Standard Deviation =", std)
plt.hist(residual_error, bins=25, density=True, alpha=0.6, color='orange')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2)
title = "2018ME20727 : Mean = %.2f,  standard deviation = %.2f" % (mean, std)
plt.title(title)

plt.show()









