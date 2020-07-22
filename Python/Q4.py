import numpy as np 

mu=0.0
sigma=1.0
X=np.random.normal(mu,sigma,size=(20,20)).astype(np.int32)
y=np.random.normal(mu,sigma,size=(20,1)).astype(np.int32)

theta=np.linalg.solve((X.T)@X,(X.T)@y)
print(theta)

