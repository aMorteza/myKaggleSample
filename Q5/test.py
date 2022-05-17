import sys
sys.path.append('../')
from config import *
from helpers import *




#-----------------------------------------------Question5-----------------------------------------------------------


weights = select_column_from_table_by_shell('Player', 'weight')

decimal_weights = []
for item in range(int(len(weights))):
	decimal_weights.append(float(weights[item]))

#Confidence Interval
print("mean confidence interval for weights of players: "),
print(mean_confidence_interval(decimal_weights, 0.99))



#Another method---------------------------------------------------------------------------------------------------------
print scipy.stats.t.interval(0.99, len(decimal_weights)-1, loc=np.mean(decimal_weights), scale=scipy.stats.sem(decimal_weights))

print("Mean: "),
print(mean(decimal_weights))
'''
this is %99 near the real mean 
'''