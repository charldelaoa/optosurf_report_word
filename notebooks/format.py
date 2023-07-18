import matplotlib.pyplot as plt

# define your custom theme as a dictionary of parameters
my_theme = {
    "figure.facecolor": "white", 
    "axes.facecolor": "white", # green
    "axes.edgecolor": "white",
    "axes.labelcolor": "#4E616A",
    "axes.grid": True,
    "grid.color": "#E0E0E0",
    "xtick.color": "black",
    "ytick.color": "black",
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Tahoma"]
}


def plot_format_plt(xlabel, ylabel, xticks, yticks, ax):
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.xaxis.set_major_locator(plt.MultipleLocator(xticks))  # Set x-axis tick frequency
    ax.yaxis.set_major_locator(plt.MultipleLocator(yticks))