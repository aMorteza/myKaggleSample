import sys
sys.path.append('../')
from config import *
from helpers import *


#---------------------------------------Question2-----------------------------------------------------------


heights = select_column_from_table_by_shell('Player', 'height')
weights = select_column_from_table_by_shell('Player', 'weight')

plt.scatter(heights, weights)
plt.show()

decimal_weights = []
for item in range(int(len(weights))):
	decimal_weights.append(float(weights[item]))


decimal_heights = []
for item in range(int(len(heights))):
	decimal_heights.append(float(heights[item]))

print("Covariance:")
print(np.cov(decimal_heights, decimal_weights))

#They are in same length:
print("Correlation:")
print (np.corrcoef(decimal_heights,decimal_weights))
print (get_correlation_of_two_vectors(decimal_heights, decimal_weights))
