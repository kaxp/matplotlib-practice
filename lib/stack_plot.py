import matplotlib.pyplot as plt


def main():
    plt.style.use("fivethirtyeight")

    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
    p2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
    p3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

    plt.stackplot(
        minutes,
        p1,
        p2,
        p3,
        labels=["player1", "player2", "player3"],
        colors=["#6d904f", "#fc4f30", "#008fd5"],
    )

    plt.legend(loc=(0.07, 0.05))
    plt.title("My Awesome Stack Plot")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
