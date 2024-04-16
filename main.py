import matplotlib.pyplot as plt
import numpy as np
import math
import time
from datetime import datetime


def draw_clock(hour, minute, second, ax):
    """Draw the clock hands on the matplotlib axes using text."""
    ax.clear()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.axis("off")

    hour_max_length = 10
    minute_max_length = 15
    second_max_length = 18

    hour_angle = (hour % 12) / 12 * 360 - 90
    minute_angle = (minute / 60) * 360 - 90
    second_angle = (second / 60) * 360 - 90

    def draw_hand(time_value, angle, max_length):
        step = max_length / 10
        for i in range(1, max_length + 1):
            x = i * math.cos(np.deg2rad(angle))
            y = i * math.sin(np.deg2rad(angle))
            ax.text(
                x,
                y,
                str(time_value),
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=8,
                color="black",
            )

    draw_hand(hour, hour_angle, hour_max_length)
    draw_hand(minute, minute_angle, minute_max_length)
    draw_hand(second, second_angle, second_max_length)


def update_clock():
    """Update the clock hands based on the current time."""
    current_time = datetime.now()
    draw_clock(current_time.hour, current_time.minute, current_time.second, ax)
    plt.draw()
    plt.pause(1)


fig, ax = plt.subplots()
plt.ion()

while True:
    update_clock()
