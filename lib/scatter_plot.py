import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

# plt.scatter(x_data, y_data)

# Make marker color to blue
# plt.scatter(x_data, y_data, c="#00f")

# Make marker as *
# plt.scatter(x_data, y_data, c="#00f", marker='*')``

# s is for marker size
# plt.scatter(x_data, y_data,  c="#00f", marker='*', s= 100)

# alpha help create transparency, so we can see heatmap when markers overlaps
plt.scatter(x_data, y_data, c="#00f", marker="*", s=100, alpha=0.3)

plt.show()
