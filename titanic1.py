import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

train = pd.read_csv("Titanic_dataset/train.csv")
test = pd.read_csv("Titanic_dataset/test.csv")

train.head(5)
test.head(5)
train.shape
test.shape
train.info()
test.info()
train.isnull().sum()
test.isnull().sum()

def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()

    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']

    df.plot(kind='bar')

bar_chart('Sex')

bar_chart('Pclass')

f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived', data =train, ax=ax[1])
ax[1].set_title('Survived')
plt.show() # pie chart

