import numpy as np
import matplotlib.pyplot as plt

# normal distribution(mean, standard deviation, count)
ages = np.random.normal(20, 1.5, 1000)

# plt.hist(ages)

# bins is number of bars(bins)
# min age to 18, 18 to 21 and 21 to max age
# plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])


# displaying cumulative result
plt.hist(ages, bins=20, cumulative=True)

plt.show()
