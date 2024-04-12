import matplotlib.pyplot as plt
import numpy as np

years = [2010, 2011, 2012, 2013, 2014, 2015]
samples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.xlabel('Year')
plt.ylabel('Yield')
plt.plot(years,samples)

import matplotlib.pyplot as plt
import numpy as np

years = range(2000,2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931,0.934,0.936,0.937,0.9375, 0.9377, 0.9380]
oranges = [0.962,0.941,0.930,0.923,0.918,0.908,0.907,0.904,0.901,0.898, 0.896, 0.894]

plt.plot(years,apples, marker = 'x')
plt.plot(years,oranges, marker = 'o')
plt.xlabel('Years')
plt.ylabel('Yield')
plt.title("Crop Yields in Kanto")
plt.legend(['Apples','Oranges'])
plt.show()

plt.figure(figsize = (9, 3))
plt.plot(years, apples, marker = 'x')
plt.show()

#ScatterPlot
import numpy as np
girls_grades = np.random.randint(100, size = 30)
boys_grades = np.random.randint(100, size = 30)
grades_range = np.random.randint(100 , size = 30)
fig = plt.figure(figsize = (3,3))
ax = fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color = 'r')
ax.scatter(grades_range, boys_grades, color = 'b')
ax.set_xlabel('Grand Range')
ax.set_ylabel('Grand Scored')
ax.set_title('Scatter Plot')
plt.show()

#Bar Graphs
years = range(2000,2006)
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
plt.xlabel('Year')
plt.ylabel('Yield')
plt.bar(years,apples)
plt.bar(years, oranges, bottom = apples )
plt.show()

data = [[30, 25, 50, 20], [40, 23, 51, 17]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b' , width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g',  width = 0.25)
ax.set_xticks([0.25, 1.25 , 2.25, 3.25])
ax.set_xticklabels([2015, 2016, 2017, 2018])
ax.legend(labels = ['Oranges', 'Apples'])
plt.show()

#Histogram
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1,1)
a = np.array([72, 87, 5, 73, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
ax.hist(a, bins = [0.25, 50, 75, 100])
ax.set_title("Histogram of result")
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel('Marks')
ax.set_ylabel('No. of students')
plt.show()