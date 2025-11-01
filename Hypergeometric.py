import numpy as np
import pandas as pd

#N is the number of balls K is the number of suucsess
#n is the number of samples

def hypergeometric(N,K,n):
    count = 0
    number_of_winners = K
    No_Total = N
    ans = 0
    while count <n:
        count +=1
        random = np.random.uniform(0,1)
        if random <= number_of_winners/No_Total:
            ans += 1
            number_of_winners += -1
            No_Total += -1
        else:
            No_Total += -1
    return ans

no_trials = 10000
N = 0
ans = []
No_sample =1000
K = 200
n =15
while N <no_trials:
    N +=1
    ans.append(hypergeometric(No_sample,K,n))

data = pd.DataFrame(ans)

print("Mean of data", data.mean())
print("Var of Data", data.var())


print("True Mean of Data", n*(K/No_sample))
print("True Variance of Data",n*(K/No_sample)*(1-(K/No_sample))*((No_sample-n)/(No_sample-1)))