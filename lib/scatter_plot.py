import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

data = pd.read_csv("lib/data/youtube_view_to_like_ratio.csv")
view_counts = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(
    view_counts,
    likes,
    c=ratio,
    cmap="summer",
    edgecolors="black",
    linewidths=1,
    alpha=0.75,
)
cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

# Show x and y label in logarithmic values to make this particualar graph better
# as without it, lot of points are overlapping on each other
plt.xscale("log")
plt.yscale("log")
plt.title("Trending Youtube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()
