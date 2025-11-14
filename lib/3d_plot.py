import numpy as np
import matplotlib.pyplot as plt


def main():
    ax = plt.axes(projection="3d")

    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)

    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    ax.plot_surface(X, Y, Z, cmap="Spectral")
    ax.set_title("3D Surface Plot")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    plt.show()


if __name__ == "__main__":
    main()
