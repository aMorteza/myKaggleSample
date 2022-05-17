from var_dump import var_dump
from config import *


import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy import stats
from scipy.stats.stats import pearsonr 


def madality(a):
	temp1 = 1
	temp2 = 0
	mod = a[0]
	for i in range(1, int(len(a))):
		if a[i] == mod:
			temp1 += 1
		elif a[i] == a[i-1]:
			temp2 += 1
		else:
			temp2 = 1
		if temp2 > temp1:
			mod = a[i]
			temp1 = temp2

	return mod

def finding_fucking_outliers_count(data):
	first = 167
	last = 195
	cnt = 0
	for item in data:
		if item > last or item < first:
			cnt += 1

	return cnt

def calculate_ages(data):
	ages = []
	for item in data:
		age = 2018 - int(item[:4])
		ages.append(age)
	return ages


def bar_graph(data):
	high, medium, low = 0, 0, 0
	for item in data:
		if item == "high":
			high += 1
		elif item == "medium":
			medium += 1
		elif item == "low":
			low += 1

	objects = ('low', 'medium', 'high')
	y_pos = np.arange(len(objects))
	performance = []
	for i in range(len(objects)):
		performance.append(0)

	performance[0] = low
	performance[1] = medium
	performance[2] = high

	plt.bar(y_pos, performance, align='center', alpha=0.9)
	plt.xticks(y_pos, objects)
	plt.ylabel('Usage')
	plt.title('Attacking Work Rate')
 
	plt.show()

def get_correlation_of_two_vectors(a, b):
	return pearsonr(a,b)



import scipy as sp
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m+h
#--------------------------------------Question1----------------------------------------------------------


# heights = select_column_from_table_by_shell('Player', 'height')

# data = []
# for item in range(int(len(heights))):
# 	data.append(float(heights[item]))

# plt.hist(heights, cumulative = True, color = 'b', alpha = 0.8)
# plt.show()

# print(madality(data))
# print(skew(data))

# plt.boxplot(data)
# plt.show()

# print(finding_fucking_outliers_count(data), int(len(data)))

#---------------------------------------Question2-----------------------------------------------------------


# heights = select_column_from_table_by_shell('Player', 'height')
# weights = select_column_from_table_by_shell('Player', 'weight')

# plt.scatter(heights, weights)
# plt.show()

# decimal_weights = []
# for item in range(int(len(weights))):
# 	decimal_weights.append(float(weights[item]))


# decimal_heights = []
# for item in range(int(len(heights))):
# 	decimal_heights.append(float(heights[item]))


# print(np.cov(decimal_heights, decimal_weights))

# #They are in same length:
# print (np.corrcoef(decimal_heights,decimal_weights))
# print (get_correlation_of_two_vectors(decimal_heights, decimal_weights))

#-----------------------------------------------Question3----------------------------------------------------------


# attacking = select_column_from_table_by_shell('Player_Attributes', 'attacking_work_rate')
# alphab = ['low', 'medium', 'high']
# frequencies = [attacking.count('low'), attacking.count('medium'), attacking.count('high')]
# pos = np.arange(len(alphab))
# width = 1.0     # gives histogram aspect to the bar diagram
# ax = plt.axes()
# ax.set_xticks(pos + (width / 2))
# ax.set_xticklabels(alphab)
# plt.title('Attacking Work Rate')
# plt.bar(pos, frequencies, width, color='b')
# plt.show()



#-----------------------------------------------Question4-----------------------------------------------------------





# weights = select_column_from_table_by_shell('Player', 'weight')

# decimal_weights = []
# for item in range(int(len(weights))):
# 	decimal_weights.append(float(weights[item]))






