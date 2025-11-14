import matplotlib.pyplot as plt


def main():
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    incomes = [55, 56, 58, 60, 65, 72, 73, 74]

    ticks = list(range(50, 82, 2))

    plt.plot(years, incomes)
    plt.title("Income of John in USD")
    plt.xlabel("Year")
    plt.ylabel("Yearly Income (USD)")
    plt.yticks(ticks, [f"${x}k" for x in ticks])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
