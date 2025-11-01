import numpy as np
import pandas as pd

def bernouli(p):
    Ran = np.random.uniform(0, 1)
    if Ran <= p:
        return 1
    else:
        return 0

counts = 0
data = []
trials = 100
while counts < (trials+1):
    data.append(bernouli(0.5))
    counts += 1
df = pd.DataFrame(data,columns = ['counts'])

print("Mean of sample",df.mean())
print("Standard Dev",df.var() )


