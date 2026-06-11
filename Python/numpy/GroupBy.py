import numpy as np
import pandas as pd

data = {
    "Dept": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
}

data = pd.DataFrame(data)

# print(data)

print(data.groupby('Dept')['Salary'].max())