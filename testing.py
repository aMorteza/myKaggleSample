# # import matplotlib.pyplot as plt; plt.rcdefaults()
# # import numpy as np
# # import matplotlib.pyplot as plt
 
# # objects = ('15-20', '20-25', '25-30', '30-35', '35-40', '40-45')
# # y_pos = np.arange(len(objects))

# # performance = [10,8,6,4,2,1]
 
# # plt.bar(y_pos, performance, align='center', alpha=0.5)
# # plt.xticks(y_pos, objects)
# # plt.ylabel('Usage')
# # plt.title('Programming language usage')
 
# # plt.show()
# import numpy as np
# import pandas as pd
# import os
# os.chdir('C:\\Users\\Greg\\Desktop\\Kaggle\\titanic') # Set working directory

# titanic_train = pd.read_csv("titanic_train.csv")      # Read the data

# char_cabin = titanic_train["Cabin"].astype(str)    # Convert cabin to str

# new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter

# titanic_train["Cabin"] = pd.Categorical(new_Cabin)  # Save the new cabin var

# my_tab = pd.crosstab(index=titanic_train["Survived"],  # Make a crosstab
#                               columns="count")      # Name the count column

# my_tab

    # hotel ratings settings
   
from var_dump import var_dump
from config import *   
import numpy as np
import matplotlib.pyplot as plt

# data = [[ 66386, 174296,  75131, 577908,  32015],
#         [ 58230, 381139,  78045,  99308, 160454],
#         [ 89135,  80552, 152558, 497981, 603535],
#         [ 78415,  81858, 150656, 193263,  69638],
#         [139361, 331509, 343164, 781380,  52269]]

attacking = select_column_from_table_by_shell('Player_Attributes', 'attacking_work_rate')
data = []
for item in range(int(len(attacking))):
	data.append(float(attacking[item]))
# data = attacking

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
# columns = ('low', 'medium', 'high')
# rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
rows = ['%s' % x for x in ('100', '50', '20', '10', '5')]

values = np.arange(len(columns))
value_increment = 1000

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')

plt.show()