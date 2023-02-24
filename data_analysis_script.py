import numpy as np
import matplotlib.pyplot as plt

# load dataset from binary
numpy_array=np.load("data/ising.npz")

with np.load("data/ising.npz") as datafile:
    spins=datafile["spins"]
    temp=datafile["temp"]

# knowing the data (2d slices of solid represented by arrays with 1 and -1) we
# can look at two magnetization and staggered magnetization for each slice:
# effectively reducing the dimensionality of the data

# build signmatrix for staggered magnetization
# low staggered magnetization means strong grouping of magnetic regimes (weisssche bezirke)
signmatrix=np.zeros(np.shape(spins))
for i in range(np.shape(spins)[1]):
    for j in range(np.shape(spins)[2]):
        signmatrix[i,j]=(-1)**(i+j)

magn=[]
smagn=[]
for i in range(np.shape(spins)[0]):
    magn.append(np.sum(spins[i])/(np.shape(spins)[1]*np.shape(spins)[2]))
    temp=0
    for j in range(np.shape(spins)[1]):
        for k in range(np.shape(spins)[2]):
            temp+=signmatrix[j,k]*spins[i,j,k]
    smagn.append(temp/(np.shape(spins)[1]*np.shape(spins)[2]))

magn=np.array(magn)
smagn=np.array(smag)

# visualizing the behaviour over temperature

plt.figure(figsize=(15,8))
plt.scatter(magn, smagn, c=temp, s=7, cmap='coolwarm')
plt.colorbar(label='temperature')
plt.title("Scatterplot of temperature")
plt.xlabel("magnetization")
plt.ylabel("staggered magnetization")
plt.show()