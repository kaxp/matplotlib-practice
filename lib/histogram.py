import pandas as pd
import matplotlib.pyplot as plt

# Histogram are a bit similar to Bar graph, the difference here is that
# we plot histogram in bins. So let's say we have hundreds of data that we
# need to plot and if using Bar or other graph its not good as the data will
# clatter. So in those conditions we use histogram where we define bins.
# For e.g if we define bins = 5, then it means over entire data in graph will
# be divided and plotted in 5 sections(bins)

plt.style.use("fivethirtyeight")

data = pd.read_csv("lib/data/ages.csv")
ids = data["Responder_id"]
ages = data["Age"]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# When result of some bars is too high, the graph can look
# a bit weird, so in that case we can change the value to
# logorithmic value using log
plt.hist(ages, bins=bins, edgecolor="black", log=True)


median_age = 28
color = "#fc4f30"

plt.axvline(median_age, color=color, label="Median Age")

plt.legend()

plt.title("Ages of responders")
plt.xlabel("Ages")
plt.ylabel("Responders")

plt.tight_layout()
plt.show()
