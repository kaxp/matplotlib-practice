import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates


def main():
    plt.style.use("seaborn-v0_8")

    data = pd.read_csv("lib/data/bitcoin_price.csv")

    # when dates are in string and not in DateTime we have to
    # convert them to DateTime using pandas
    data["Date"] = pd.to_datetime(data["Date"])
    data.sort_values("Date", inplace=True)

    price_date = data["Date"]
    price_close = data["Close"]

    plt.plot_date(price_date, price_close, linestyle="solid")

    # get current figure and auto format on x axis dates
    plt.gcf().autofmt_xdate()

    plt.title("Bitcoin Price")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")

    # Formatting the date like May, 19 2024
    fmt = mpl_dates.DateFormatter("%b, %d %Y")
    plt.gca().xaxis.set_major_formatter(fmt)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
