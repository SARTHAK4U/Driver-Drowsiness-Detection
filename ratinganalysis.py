
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv("Record.csv")

print(df[['Name','Average Drowsiness Count','Average Yawn Count']])

df = df.groupby('Name', as_index=False).agg({'Average Drowsiness Count':'mean', 'Average Yawn Count':'mean'}).reset_index()
print(df[['Name','Average Drowsiness Count','Average Yawn Count']])




"""# **FORMULA FOR RATING**

(3.5 x Average Drowsiness Count+1.5 x Average Yawn Count)
"""

a=df["Average Drowsiness Count"]
b=df["Average Yawn Count"]

sum_column =(3.5*a+ 1.5*b)
print(sum_column)


plt.stem(df["Name"],sum_column,use_line_collection=True)
plt.xlabel('NAME OF DRIVER') 
plt.ylabel('RATING') 
plt.title('ANALYSIS') 
plt.grid(True)
plt.savefig('RATINGS.png')
plt.show()




"""# PICKING BEST DRIVER"""
min=60000
pos=0
count=0
for x in sum_column:
  if x<min:
    min=x
    pos=count
  count+=1

print('CURRENT BEST DRIVER IS :')
print(df['Name'].iloc[pos])
print("RATING IS : "+str(sum_column[pos]))