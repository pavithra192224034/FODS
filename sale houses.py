import numpy as np
h= np.array([
    [4,2000,25000],
    [5,2400,300000],
    [3,18000,200000],
    [5,2800,35000],
    ])
b=h[h[:,0]>4]
s=b[:,2]
a=np.mean(s)
print(f"the average sale price of houses with more than four bedrooms is : {a}")
