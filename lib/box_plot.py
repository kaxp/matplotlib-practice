import numpy as np
import matplotlib.pyplot as plt


# Box plot is stastical part showing the different
# Quartiles, Median, Maximum, Minimum and Outliers.
def main():
    first = np.linspace(0, 10, 25)
    second = np.linspace(10, 200, 25)
    third = np.linspace(200, 210, 25)
    fourth = np.linspace(210, 230, 25)

    data = np.concatenate((first, second, third, fourth))

    plt.boxplot(data)
    plt.title("Box Plot")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
