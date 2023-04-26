#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import pandas
import pandas as pd
  
# State the list of lists
data = [['Monday', 198, 20, 'sunny'], ['Tuesday', 324, 30, 'sunny'], ['Wednesday', 275, 30, 'sunny'], 
        ['Thursday', 346, 32, 'sunny'], ['Friday', 126, 10, 'rainy'], ['Saturday', 146, 13, 'gloomy'], 
        ['Sunday', 63, 5, 'rainy']]
  
# Create DataFrame
df = pd.DataFrame(data, columns=['day', 'calories_burnt', 'time_min', 'weather'])
  
# Print
df


# In[3]:


# Sorting & filtering
df_sort = df.sort_values(by='time_min')
df_sort

#df_sort = df.sort_values(by='time_min', ascending=False)
#df_sort

df_short = df[df.time_min<=20]
df_short


# In[4]:


# Making a Plot
import pandas as pd
from matplotlib import pyplot as plt

plt.figure(figsize =(10, 7))

for count, data in enumerate(df.time_min):
    plt.text(y=data+1,
             x=count-0.1,
             s=f"{data}", color='black',
             va='center', fontweight='bold')

# Horizontal Bar Plot
plt.bar(df.day, df.time_min)
plt.xlabel("Days")
plt.ylabel("Spent time (in minutes)")

plt.savefig("plot_2.png")
 
# Show Plot
plt.show()


# In[6]:


# Reading a CSV file
import time
import pandas as pd

def csv_reader():
    read_file = pd.read_csv('Significant_Earthquakes.csv', delimiter=',')
    print(read_file)
init_time = time.time()
cr=csv_reader()
final_time= time.time()
print('It took the CSV reader', "%.4f" %(final_time - init_time), 'seconds to read the file')


# In[ ]:





# In[ ]:




