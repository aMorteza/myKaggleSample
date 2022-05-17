import sys
sys.path.append('../')
from config import *
from helpers import *

#-----------------------------------------------Question3----------------------------------------------------------


attacking = select_column_from_table_by_shell('Player_Attributes', 'attacking_work_rate')
alphab = ['low', 'medium', 'high']
frequencies = [attacking.count('low'), attacking.count('medium'), attacking.count('high')]
pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)
plt.title('Attacking Work Rate')
plt.bar(pos, frequencies, width, color='b')
plt.show()

#Frequecy Table
print('-----------------------------')
print ('attacking_work_rate    count')
print('-----------------------------')
print('low                   '),
print(attacking.count('low'))
print('-----------------------------') 
print('mediu                 '),
print(attacking.count('medium'))
print('-----------------------------') 
print('high                   '),
print(attacking.count('high'))
print('-----------------------------') 