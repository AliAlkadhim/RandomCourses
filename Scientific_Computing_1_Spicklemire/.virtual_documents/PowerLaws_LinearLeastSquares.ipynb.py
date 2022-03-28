import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


x = np.linspace(0,10, 100)
plt.xlabel('x')
y=  x + np.random.randn(100)
plt.ylabel('y')
plt.scatter(x,y)


M = np.array([x, np.ones(x.shape)]); print(M, M.shape)


plt.hist(x)



