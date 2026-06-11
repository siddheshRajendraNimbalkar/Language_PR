import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.randint(0,9,11),
    'B': np.random.randint(0,9,11),
    'C': np.random.randint(0,9,11),
})

# print(df)

print(df.loc[:2])
print(df.iloc[:2])
print(df.iloc[:,:-2])

