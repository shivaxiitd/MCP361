#Assignment 6
#Problem 1
#Siddharth Dixit
#2018ME20727

import numpy as np
import math
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

n = 100

# a = 0.2 & b = 0.3
# ab =[a, b]
ab = [0.2, 0.3]

#mean 0 and standard deviation 0.5
#msd = [mean, standard deviation]
msd = [0, 0.5]

X = np.linspace(1,50,n)
s = np.random.normal(msd[0], msd[1], n)
y = []

x = 0
while x < n:
    y.append(ab[0] + ab[1]*X[x] + s[x])
    x = x + 1

x_train,x_test,y_train,y_test=train_test_split(X.reshape(-1, 1),y,test_size=0.2)

regression = LinearRegression().fit(x_train, y_train)
print("Regression Score =",regression.score(x_test,y_test))
intercept = regression.intercept_
slope = regression.coef_

print("Slope = ", slope)
print("Intercept = ", intercept)


y_pred = []
for xi in x_test:
    y_pred.append(regression.predict(xi.reshape(-1, 1))[0])



X_axis = np.arange(len(x_test))
plt.bar(X_axis-0.2, y_pred,0.4, label = 'Predicted')
plt.bar(X_axis+0.2, y_test,0.4, label = 'Correct')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2018ME20727 : Comparison using Bar-chart")
plt.legend(loc='best')
plt.show()







