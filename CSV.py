import pandas as pd

path='C:/Users/Shadia/OneDrive/Desktop/L/Machine Learning/CsvData/bank-KNN.csv'
print("Basic use:")
data=pd.read_csv(path,sep=';')
print(data.head())

print("Custom header:")
df=pd.read_csv(path,header=1,sep=';')
print(df.head())

print("Custom column Name:")
df=pd.read_csv(path,sep=';',names=['A','B','C','D'])
print(df.head())

print("Setting index column:")
df=pd.read_csv(path,sep=';',index_col=0)
print(df.head())

print("Selecting columns:")
df = pd.read_csv(path,sep=';',usecols=['age','job'])
print(df.head())


print("Setting data types:")
df=pd.read_csv(path,sep=';',dtype={'pdays':float})
print(df.info())

print("Skipping Rows:")
df=pd.read_csv(path,sep=';',skipfooter=2,engine='python')
print(df.head())


print("print limited rows:")
df=pd.read_csv(path,sep=';',nrows=10)
print(df)

print("Handeling missing values:")
df=pd.read_csv(path,sep=';',na_values=['NA','NULL','-1'])
print(df.isnull().sum())

print("Using iterator and chuncksize:")
df=pd.read_csv(path,sep=';',chunksize=1000)
for i in df:
    print(i.shape)
    
print("Handling bad lines:")
df=pd.read_csv(path,sep=';',on_bad_lines='skip')
print(df.head())

print("Handling Dialect and Quotechar:")
df= pd.read_csv(path,sep=';', quotechar='"')
print(df.head())

print("Low Memory Optimization:")
df= pd.read_csv(path,sep=';', low_memory=False)
print(df.info())

print("Custom Encoding:")
df= pd.read_csv(path,sep=';', encoding='utf8')
print(df.head())

print("Handling Comments:")
df= pd.read_csv(path,sep=';', comment='#')
print(df.head())