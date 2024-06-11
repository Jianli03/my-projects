# In Machine Learning (and in mathematics) there are often three values that interests us:

# Mean - The average value
# Median - The mid point value
# Mode - The most common value

import os
import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(f"The mean speed is {x}")

x = numpy.median(speed)
print(f"The median speed is {x}")

x = stats.mode(speed)
print(f"The mode speed is {x}")


# Standard Deviation is often represented by the symbol Sigma: σ

# Variance is often represented by the symbol Sigma Squared: σ2

# Standard deviation is a number that describes how spread out the values are.

# A low standard deviation means that most of the numbers are close to the mean (average) value.

# A high standard deviation means that the values are spread out over a wider range.

speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(f"Speed Deviation is low as {x}" )

speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(f"Speed Deviation is high as {x}" )

# Variance is another number that indicates how spread out the values are.
# In fact, if you take the square root of the variance, you get the standard deviation!
# Or the other way around, if you multiply the standard deviation by itself, you get the variance!
x = numpy.var(speed)
print(f"Variance of speed is {x}" )


# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)
print(f" What is the 75. percentile? The answer is {x}, meaning that 75% of the people are 43 or younge")

# Random Data Distributions
# Create an array containing 250 random floats between 0 and 5:
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
# To visualize the data set we can draw a histogram with the data we collected.
plt.hist(x, 5)
plt.show()


#Normal data distribution, or the Gaussian data distribution,
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

# The x array represents the age of each car.
#The y array represents the speed of each car.
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()


# Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
# The first array will have the mean set to 5.0 with a standard deviation of 1.0.
# The second array will have the mean set to 10.0 with a standard deviation of 2.0:
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

# Line of Linear Regression
# Import scipy and draw the line of Linear Regression:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# How well does my data fit in a linear regression?
# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.
# This relationship - the coefficient of correlation - is called r
print(f"The coefficient of correlation is r = {r}")

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


#Line of polynomial regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

#R-Squared is how well the relationship between the values of the x- and y-axis is.
# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
# Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))

# predict future values.
# predict the speed of a car that passes the bollboooth at around 17:00
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
speed = mymodel(17)
print(speed)


print("Current Working Directory:", os.getcwd())
print("Files in the current directory:", os.listdir('.'))



# Multiple regression - predict a value based on two or more variable
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(f"predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:  {predictedCO2} ")

print(regr.coef_)


# There are different methods for scaling data, in this tutorial we will use a method called standardization.

# The standardization method uses this formula:

# z = (x - u) / s

# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.
scale = StandardScaler()
df = pandas.read_csv("data.csv")
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)
print(scaledX)

#Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)