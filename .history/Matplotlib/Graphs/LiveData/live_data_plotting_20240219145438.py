from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.xkcd()
x_vals = []
y_vals = []
index = count()


import pandas as pd
import matplotlib.pyplot as plt

def animate(i):
    """
    Function to animate the live data plotting.

    Parameters:
    - i (int): The frame number for the animation.

    Returns:
    - None
    """
    # Read the data from the CSV file
    data = pd.read_csv('data.csv')

    # Extract the x and y values from the data
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    # Clear the current plot
    plt.cla()

    # Plot the data for Channel 1 and Channel 2
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    # Add legend to the plot
    plt.legend(loc='upper left')

    # Adjust the layout of the plot
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
