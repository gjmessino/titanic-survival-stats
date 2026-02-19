import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/Vidit-Bhatwadekar/Titanic_Project/main/titanic_project.csv", index_col="PassengerId").drop(["Cabin"], axis=1)
titanic.head()
titanic.info()

for column in ['Sex', 'Embarked']:
  titanic[column] = titanic[column].astype('category') # converting columns to category
cleaned_titanic = titanic.dropna()
cleaned_titanic.info()
cleaned_titanic.groupby('Survived').agg('mean', numeric_only=True)

titanic_survivors = titanic[titanic['Survived'] == 1]
titanic_nonsurvivors = titanic[titanic['Survived'] == 0]

plt.hist(titanic_survivors['Age'])
plt.hist(titanic_nonsurvivors['Age'], alpha = 0.8)
plt.title('Number of passengers by age group')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()

plt.bar(titanic_survivors['Pclass'], titanic_survivors['Fare'], alpha = .4, color = 'pink', label = 'Survived')
plt.bar(titanic_nonsurvivors['Pclass'], titanic_nonsurvivors['Fare'], alpha = .4, color = 'purple', label = 'Died')
plt.title('Survival by Class and Fare')
plt.xlabel('Class')
plt.ylabel('Fare')
plt.show()

#Do not edit this cell
# using .value_counts() to separate out survivors/non_survivors by sex
survivors_by_sex = titanic_survivors['Sex'].value_counts()
nonsurvivors_by_sex = titanic_nonsurvivors['Sex'].value_counts()

# plotting
plt.bar(survivors_by_sex.index, survivors_by_sex.values)
plt.title('Number of survivors by sex')
plt.xlabel('Sex')
plt.ylabel('Number of passengers')
plt.show()

plt.bar(nonsurvivors_by_sex.index, nonsurvivors_by_sex.values)
plt.title('Number of nonsurvivors by sex')
plt.xlabel('Sex')
plt.ylabel('Number of passengers')
plt.show()

plt.bar(titanic_survivors['Survived'], titanic_survivors['Parch'], color = 'pink')
plt.bar(titanic_nonsurvivors['Survived'], titanic_nonsurvivors['Parch'], color = 'purple')
plt.xlabel('Survived')
plt.ylabel('Parch')
plt.title('Survival Rates by Parents and Children')
plt.show()

plt.bar(titanic_survivors['Survived'], titanic_survivors['SibSp'], color = 'green')
plt.bar(titanic_nonsurvivors['Survived'], titanic_nonsurvivors['SibSp'], color = 'yellow')
plt.xlabel('Survived')
plt.ylabel('Siblings')
plt.title('SibSp by Survived')
plt.show()

counts_surv = titanic_survivors['Embarked'].value_counts()
categories = counts_surv.index
values_surv = counts_surv.values
plt.bar(categories, values_surv,  alpha = 0.5, color = 'green', label = 'Survived')
counts_nonsurv = titanic_nonsurvivors['Embarked'].value_counts()
categories = counts_nonsurv.index
values_nonsurv = counts_nonsurv.values
plt.bar(categories, values_nonsurv,alpha = 0.5, color = 'purple', label = 'Died')
plt.title('Embarked by Survived')
plt.xlabel('Embarked')
plt.ylabel('Number of Passengers')
plt.show()

plt.hist(titanic_survivors['Fare'], alpha = 0.8)
plt.hist(titanic_nonsurvivors['Fare'], alpha = 0.8)
plt.title('Fare by Survived')
plt.xlabel('Fare')
plt.ylabel('Number of Passengers')
plt.show()
