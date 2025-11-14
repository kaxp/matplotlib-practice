import matplotlib.pyplot as plt


def main():
    languages = ["Python", "C++", "C#", "Java", "Go"]
    votes = [45, 19, 8, 28, 35]
    explodes = [0, 0, 0.2, 0, 0]

    # explodes is to highlight a particular cell
    # autopct is to write the percentage in chart
    # pctdistance is distance from center
    # startangle is to define angle where to start the chart
    plt.pie(
        votes,
        labels=languages,
        explode=explodes,
        autopct="%.2f%%",
        pctdistance=0.8,
        startangle=90,
    )

    plt.title("Language Popularity")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
