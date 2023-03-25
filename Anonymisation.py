import pandas as pd
import numpy as np
import random as rd
from random import randrange

# Methods
def regionGeneralyze(region):
    if region[0] == "s":
        return "South"
    else:
        return "North"

def ageGeneralyze(age):
    if age <= 30:
        return 18
    elif age <= 45:
        return 31
    else:
        return 46

def randAge(age):
    randNumb = randrange(0,2)
    if randNumb == 0:
        return age - randrange(0,3)
    else:
        return age + randrange(0,3)

def randBmi(bmi):
    randNumb = randrange(0,2)
    if randNumb == 0:
        return bmi - rd.uniform(0,0.56)
    else:
        return bmi + rd.uniform(0,0.57)

def randChild(child):
    randNumb = randrange(0,2)
    if randNumb == 0 & child != 0:
        return child - 1
    elif randNumb == 1 & child != 5:
        return child + 1
    else:
        return child

def randCharges(charges):
    randNumb = randrange(0,2)
    if randNumb == 0:
        return int(charges) - randrange(0,146)
    else:
        return int(charges) + randrange(0,173)


# Read Initial Dataset
df = pd.read_csv("data_init.csv")

# Generalyze the region:
df["region"] = df["region"].apply(lambda x: regionGeneralyze(x))

# Adding small random bmi
df["bmi"] = df["bmi"].apply(lambda x: randBmi(x))

# Adding small random charges
df["charges"] = df["charges"].apply(lambda x: randCharges(x))

# Generalyze Age
df["age"] = df["age"].apply(lambda x: ageGeneralyze(x))

# Adding small random child
df["children"] = df["children"].apply(lambda x: randChild(x))

# Changing Dataset Order & Reseting Indec
df = df.sample(frac=1)
df=df.reset_index()
df["id"]=df.index

# Creation Index Link Dataset
df_join = df.iloc[:, [0,1]]
df_join.columns = ["Id Initial", "Id Anonym"]
df = df.iloc[:, [1,2,3,4,5,6,7,8]]

# Outputing CSVs
df.to_csv('insuranceAnno.csv', index=False)
df_join.to_csv("index_join.csv", index=False)