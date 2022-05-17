import sys
sys.path.append('../')
from config import *
from helpers import *



def mean(arr1, arr2):
  mean = []
  for i in range(len(arr1)):
    mean.append(arr1[i]/arr2[i])
  return mean

def var(arr):
  var = []
  for i in range(len(arr)):
    var.append(np.var(arr[i]))
  return var

def calculate_ages(data):
  ages = []
  for item in data:
    age = 2018 - int(item[:4])
    ages.append(age)
  return ages
  
def cal_heights_weights(data, heights, weights, performance, var_h, var_w):
  objects = ('15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50')
  y_pos = np.arange(len(objects))
  for i in range(len(objects)):
    performance.append(0)
    height.append(0)
    weight.append(0)
    var_h.append([])
    var_w.append([])
  for item in calculate_ages(data):
    if item >= 15 and item < 20:
      height[0] += heights[item]
      weight[0] += weights[item]
      var_h[0].append(heights[item])
      var_w[0].append(weights[item])
      performance[0] += 1
    elif item >= 20 and item < 25:
      performance[1] += 1
      height[1] += heights[item]
      weight[1] += weights[item]
      var_h[1].append(heights[item])
      var_w[1].append(weights[item])
    elif item >= 25 and item < 30:
      performance[2] += 1
      height[2] += heights[item]
      weight[2] += weights[item]
      var_h[2].append(heights[item])
      var_w[2].append(weights[item])
    elif item >= 30 and item < 35:
      performance[3] += 1
      height[3] += heights[item]
      weight[3] += weights[item]
      var_h[3].append(heights[item])
      var_w[3].append(weights[item])
    elif item >= 35 and item < 40:
      performance[4] += 1
      height[4] += heights[item]
      weight[4] += weights[item]
      var_h[4].append(heights[item])
      var_w[4].append(weights[item])
    elif item >= 40 and item < 45:
      performance[5] += 1
      height[5] += heights[item]
      weight[5] += weights[item]
      var_h[5].append(heights[item])
      var_w[5].append(weights[item])
    if item >= 45 and item < 50:
      performance[6] += 1
      height[6] += heights[item]
      weight[6] += weights[item]
      var_h[6].append(heights[item])
      var_w[6].append(weights[item])
    

  # plt.bar(y_pos, performance, align='center', alpha=0.9)
  # plt.xticks(y_pos, objects)
  # plt.ylabel('Usage')
  # plt.title('Number Of Players In Deferent Ages')
 
  # plt.show()



heights = select_column_from_table_by_shell('Player', 'height')
weights = select_column_from_table_by_shell('Player', 'weight')
birthdays = select_column_from_table_by_shell('Player', 'birthday')
h = []
for item in range(int(len(heights))):
  h.append(float(heights[item]))

w = []
for item in range(int(len(heights))):
  w.append(float(heights[item]))
performance = []
height = []
weight = []
var_h = []
var_w = []
cal_heights_weights(birthdays, h, w, performance, var_h, var_w)
# print(height, performance)
N = 7
meanHeights = mean(height, performance)
meanWeights = mean(weight, performance)
heightsVar = var(var_h)
weightsVar = var(var_w)
# print(heightsVar, weightsVar)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
# print(tuple(meanHeights))
p1 = plt.bar(ind, tuple(meanHeights), width, yerr=heightsVar)
p2 = plt.bar(ind, tuple(meanWeights), width,
             bottom=meanHeights, yerr=weightsVar)

plt.ylabel('Heights & Weights')
plt.title('Heights & Weights by ages of players')
plt.xticks(ind, ('15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45- 50'))
plt.yticks(np.arange(0, 500, 100))
plt.legend((p1[0], p2[0]), ('Heights', 'Weights'))

plt.show()
