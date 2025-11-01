import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Exponential(lam):
    U = np.random.uniform(0, 1)
    X = - (1/lam) * np.log(U)
    return X

def Poisson_RV(lam, T):
    count = 0
    total_time = 0
    while True:
        total_time += Exponential(lam)
        if total_time > T:
            break
        count += 1
    return count

# Simulation parameters
trials = 10000
lambdas = [0.5, 1, 47]
time = 1

# Generate Poisson samples
poisson_list = []
for _ in range(trials):
    row = [Poisson_RV(lam, time) for lam in lambdas]
    poisson_list.append(row)

data = pd.DataFrame(poisson_list, columns=[f"λ={lam}" for lam in lambdas])

colors = ['k', 'r', 'b', 'g']

for col, color in zip(data.columns, colors):
    counts, bins = np.histogram(data[col], bins='auto')
    centers = 0.5 * (bins[1:] + bins[:-1])
    plt.stem(centers, counts, basefmt=" ", linefmt=color+'-', markerfmt=color+'o',
              label=col)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Poisson(λT) Distributions via Exponential Simulation")
plt.legend()
plt.show()

print("Mean of list", data.mean())
print("Var of list", data.var())