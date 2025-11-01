import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Okay we can get an expoential RV from a Uniform by completing this transform
# So expential tells us a contious valeu of time until the evnt ocucrs

def Exponential(lam):
    U = np.random.uniform(0, 1)
    X = - (1/lam) * np.log(U)
    return X

Lambda = 0.2
N= 0
List_of_expo =  []
N_trials = 1000

while N < N_trials:
    N += 1
    List_of_expo.append(Exponential(Lambda))

data = pd.DataFrame(List_of_expo)


plt.hist(data)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Values")
plt.show()





print("Data Mean", data.mean())
print("Data Var", data.var())
print("True mean", 1/Lambda)
print("True Variance", (1/(Lambda**2)))

