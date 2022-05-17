import sys
sys.path.append('../')
from config import *
from helpers import *

#I Choosed this Big Data Sample, because real relations of type Sql, many out of mean datas which is usually happens in real life!   
#--------------------------------------Question1----------------------------------------------------------


heights = select_column_from_table_by_shell('Player', 'height')

data = []
for item in range(int(len(heights))):
	data.append(float(heights[item]))

plt.hist(heights, cumulative = True, color = 'b', alpha = 0.8)
plt.show()

print(madality(data))
print(skew(data))

plt.boxplot(data)
plt.show()

print(finding_fucking_outliers_count(data), int(len(data)))
