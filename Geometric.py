import numpy as np
import pandas as pd


###This is justa negatiev binomial but r = 1####


def bernouli(p):
    Ran = np.random.uniform(0, 1)
    if Ran <= p:
        return 1
    else:
        return 0

def Geometric(p):
    count = 0
    succ = 0
    while succ ==0:
        count +=1
        outcome = bernouli(p)
        if outcome == 1:
            succ+=1
    return count

prob = 0.4
no_trials =100000
N = 0
Geo_list = []

while N < no_trials:
    N +=1
    Geo_list.append(Geometric(prob))

data = pd.DataFrame(Geo_list)

print("Mean of Geo", data.mean())
print("Var of Geo", data.var())
print("True Mean",1/prob)
print("True Var",(1-prob)/(prob**2))

