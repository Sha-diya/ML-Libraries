import numpy as np
import pandas as pd

#1:Create data
data={
      'EmpId':[1,2,3,4,5],
      'Name':['A','B','C','D','E'],
      'Age':[20,25,35,30,40],
      'Dept':['HR','IT','Finance','HR','IT'],
      'Salary':[50000,45000,48000,30000,55000],
      'Start_Date':pd.to_datetime(['2015-01-01', '2016-05-23', '2017-07-15', '2018-02-10', '2019-03-08']),
      'Performance':['Good','Fine','Ok','Excellent','Good'],
      'Hobbies':[['Reading','Sleeping'],['Sports','Photography'],['Singing'],['Music','Travalling'],['Cooking','Crafting']]
      }
df=pd.DataFrame(data)
print("\nData of the Employee:\n",df)

#2:Handling time 
df['YearWithCompany']=(pd.to_datetime('today')-df['Start_Date']).dt.days//365
print("\nEmployee data with Years with the company:\n",df)

#3:Pivot Table(Salary by department)
pivot_table=df.pivot_table(values='Salary',index='Dept',aggfunc='mean')
print("\nAverage salary by department:\n",pivot_table)

#4:Rolling window calculation(3-Years moving average salary)
df['RollingAbgSalary']=df['Salary'].rolling(window=3).mean()
print("\nEmployee salary with rolling window:\n",df)

#5:Query data
filtered_df=df.query('Age>=30')
print(filtered_df)

print(df.info())
#6:Handling categorical data
df['Dept']=df['Dept'].astype('category')
print(df.info())

#7:Exploding list data
df_exploded=df.explode('Hobbies')
print(df_exploded)

#8: ranking salaries
df['SalaryRank']=df['Salary'].rank()
print(df)


#9:MultiIndex
df.set_index(['Age','Salary'])
print(df)


#10:cross tabulation
crosstab=pd.crosstab(df['Dept'], df['Performance'])
print(crosstab)

#11:String Operation
df['Name_Upper'] = df['Name'].str.lower()
print("\nEmployee Data with Uppercase Names:\n", df)

#12:Add a new column with full name
df['FullName']=df['Name']+' '+df['Performance']
print(df['FullName'])

#13:Replace value
df['Performance']=df['Performance'].replace('Good','Average')
print(df['Performance'])

#14:Handle Missing data
df.loc[2,'Salary']=np.nan
print(df)
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print(df)

#15:sort data by salary
df=df.sort_values(by='Salary',ascending=False)
print(df)

#16:save data to csv
df.to_csv('Employee_data.csv',index=True)
print("Data saved")
