import numpy as np
import pandas as pd

##Thsi is the nuber of trials till r succsesses

def bernouli(p):
    Ran = np.random.uniform(0, 1)
    if Ran <= p:
        return 1
    else:
        return 0

def neg_bino(p,r):
    succsess = 0
    count = 0
    while succsess < r:
        count+=1
        trial = bernouli(p)
        if trial == 1:
            succsess+=1
    return count

prob = 0.4
r =5
no_trials = 100000
N = 0
Neg_Bino_List = []

while N < no_trials:
    N+=1
    Neg_Bino_List.append(neg_bino(prob,r))

data = pd.DataFrame(Neg_Bino_List)

print("Mean of negative Bino", data.mean())
print("Var of negative Bino", data.var())
print("true mean ", (r/prob))
print("True variance",(r*(1-prob)/(prob**2)))

