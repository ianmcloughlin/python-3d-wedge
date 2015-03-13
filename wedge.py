import numpy as np
import matplotlib.pyplot as pl
import mpl_toolkits.mplot3d.art3d as pl3d


fig = pl.figure()
ax = fig.gca(projection='3d')

x = np.arange(-np.pi, np.pi, 0.01)
y = np.sin(5.0 * x)
z = np.zeros(x.size)

pl.hold(True)
ax.plot(x, y, z)

poly = zip(x, y, z)
coll = pl3d.Poly3DCollection([poly])
ax.add_collection3d(coll)

pl.show()
