import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y = np.loadtxt('y.txt')

plt.subplot(2,1,1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2,1,2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.savefig('3.2.pdf')
plt.savefig('3.2.eps')
plt.show()