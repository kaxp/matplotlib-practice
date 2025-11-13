import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#! To run this program, first need to run below command to start generating dynamic data
#! for live data feed.
#! in lib/data/ run `python dynamic_data_gen.py``
#! when finish, stop the data generation

plt.style.use("seaborn-v0_8")

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv("lib/data/dynamic_data_gen.csv")
    x = data["x_value"]
    y1 = data["total_1"]
    y2 = data["total_2"]

    # Clear axis before plotting the updated graph
    plt.cla()

    plt.plot(x, y1, label="Channel 1")
    plt.plot(x, y2, label="Channel 2")

    plt.legend(loc="upper left")
    plt.tight_layout()


# interval is in milliseconds
# gcf => get current figure
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
