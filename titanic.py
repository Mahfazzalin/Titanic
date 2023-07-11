import pandas as pd #import pandas for dataframe
import matplotlib.pyplot as plt #import matplotlib for data visualigation
#%matplotlib inline  #this is an magic function
import seaborn as sns  #import seaborn for data visualigation
sns.set()

train =pd.read_csv("Titanic_dataset/train.csv")  #read train dataset and store in train variable
test =pd.read_csv("Titanic_dataset/test.csv")  #read test dataset and store in test variable

train.head(5)   #it will show train dataset 1st five row
test.head(5)     #it will show test dataset 1st five row
train.shape      #it will show the shape of train dataset
test.shape        #it will show the shape of train dataset
train.info()   #it will show the info of train dataset
test.info()     #it will show the info of test dataset
train.isnull().sum()    # "Age cabin and Embarked -> data missing" 
test.isnull().sum()     # Age cabin and Fare -> data missing
#this bar_chart is for create bar chart 
def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()

    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']

    df.plot(kind = 'bar')
#bar_chart function call to see bar graph 
bar_chart('Sex')

bar_chart('Pclass')

#this code is for pie chart , there is no function declair
f, ax = plt.subplots(1,2, figsize =(18,8))
train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0], shadow = True )
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived', data=train,ax=ax[1])
ax[1].set_title('Survived')
print(plt.show())
