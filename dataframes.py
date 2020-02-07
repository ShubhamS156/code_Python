import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame({'name':['vijay','kushal','arnav','rohan'],
                'occupation':['actor','singer','dancer','athlete'],
                'age':['21','23','12','51'],
    })
testList=[100,200,300,44.4]
print(df)
market_df=pd.read_csv("file.csv")
print(market_df)
print(market_df.info())
print(market_df.describe()) 
print(market_df.columns) #gives column names
market_df.set_index('Series_reference',inplace=True) # sets custom index
print(market_df.shape) #gives rows and columns
market_df.sort_index(axis=0,ascending=False)
print(market_df.sort_index(axis=0,ascending=False))
print(market_df.sort_values(by='Period'))
print(market_df[0:3]) #selects rows from 0 to 3 and all columns.
#print(market_df[0:3,1:2] #  invalid key ....cannot select columns like this.
print(market_df.Period)
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
print(market_df.loc[market_df.Period>10])
print(market_df.loc[market_df.Data_value.isin(testList),:])
print("iloc")
print(market_df.iloc[[14,12],2:3])
#print(market_df.loc[3,'Period'])
print(df)
def ageCheck(x):
        y='shubh'+(x)
        return y
        
df['nameMod']=df.age.apply(ageCheck)
print(market_df.info())
plt.xlabel('Current')
plt.ylabel('voltage')
plt.title('OhmsLaw')
plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.show()

plt.xlabel('a')
plt.ylabel('b')
x=np.linspace(1,10,100)
y=np.log(x)
plt.figure(1)
plt.subplot(121)
plt.title('y=log(x)')
plt.plot(x,y,x,y**2)
plt.subplot(122)
plt.title("y=log(x)**2")
plt.scatter(market_df['Period'],market_df['STATUS'])
plt.show()
print(x)
image=plt.imread('359043.jpg')
plt.imshow(image)
plt.show()
