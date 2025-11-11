import matplotlib.pyplot as plt
import random

heads_tails = [0, 0]

for _ in range(100000):
    # Add 1 to heads or tails
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])

    # plt.pause is used to animate the plot diagram, it adds a delay before the showing the graph
    plt.pause(0.001)

plt.show()
