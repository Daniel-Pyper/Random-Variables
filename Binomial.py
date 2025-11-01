import numpy as np
import pandas as pd



def binomial(p,n):
    count = 0
    trial = 0
    while trial < n:
        trial +=1
        ran = np.random.uniform(0, 1)
        if ran <= p:
            count +=1
        else:
            count+=0
    return count

Binomial_List = []

N = 0
no_trials = 10000
prob = 0.6
nn = 20
while N < no_trials:
    N +=1
    Binomial_List.append(binomial(prob,nn))
data = pd.DataFrame(Binomial_List)
print(N)
print("Mean of sample", data.mean())
print("Var of sample", data.var())
print("True mean",nn*prob)
print("True Variance", nn*prob*(1-prob))