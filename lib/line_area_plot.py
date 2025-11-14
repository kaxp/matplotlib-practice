import pandas as pd
import matplotlib.pyplot as plt


def main():
    plt.style.use("seaborn-v0_8")

    data = pd.read_csv("lib/data/salary.csv")

    ages = data["Age"]
    dev = data["All_Devs"]
    py = data["Python"]

    plt.plot(ages, dev, linestyle="--", color="#444444", label="All Devs")
    plt.plot(ages, py, label="Python")

    plt.fill_between(
        ages, py, dev, where=(py > dev), interpolate=True, alpha=0.25, label="Above Avg"
    )
    plt.fill_between(
        ages,
        py,
        dev,
        where=(py <= dev),
        interpolate=True,
        color="red",
        alpha=0.25,
        label="Below Avg",
    )

    plt.title("Median Salary (USD) by Age")
    plt.xlabel("Age")
    plt.ylabel("Median Salary")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
