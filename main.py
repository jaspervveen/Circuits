import BuildCircuit
import numpy as np
import matplotlib.pyplot as plt

L = 400e-9
C = 0.3e-12
R = 3e4


f = np.linspace(1e6, 1000e6, 1000)

Circuit = BuildCircuit.BuildCircuit()

G = np.zeros((2,len(f)))
for i in range(len(f)):
    Z_RC = Circuit.add_parallel(Circuit.zc(2*np.pi*f[i], C), R)
    Z_RLC = Circuit.add_series(Circuit.zl(2*np.pi*f[i], L), Z_RC)
    G[0,i] = np.real(Circuit.calc_gamma(Z_RLC, 50))
    G[1,i] = np.imag(Circuit.calc_gamma(Z_RLC, 50))

plt.plot(f, G[0,:])
plt.plot(f, G[1,:])
plt.show()

