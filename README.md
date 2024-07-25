![clock](https://github.com/user-attachments/assets/b08d47ad-9b70-4014-b9ab-ea3900829cd9)

# Matplotlib-based Analog Clock Visualization

This script creates a real-time updating analog clock using Matplotlib. I saw this in a tiktok and felt like doing it. It uses Python libraries such as `matplotlib`, `numpy`, and `datetime` to draw the clock hands and update them every second to reflect the current time.

## Features

- **Analog Clock Display**: Visualizes the current time with hour, minute, and second hands.
- **Real-Time Update**: Continuously updates the clock every second to show the current time.

## Requirements

- Python 3
- Matplotlib (`matplotlib`)
- Numpy (`numpy`)

## Setup

1. **Install Dependencies**: Use `pip install matplotlib numpy`.
2. **Run the Script**: Execute `python main.py` to start the analog clock visualization.

## Usage

- **Real-Time Clock Visualization**: The script runs an infinite loop that updates the clock every second to display the current time.

## Customization

- **Clock Hand Lengths**: You can customize the lengths of the hour, minute, and second hands by modifying the `hour_max_length`, `minute_max_length`, and `second_max_length` variables in the `draw_clock` function.

## Notes

- Ensure that your Python environment has the required libraries installed.
- The script uses Matplotlib's interactive mode (`plt.ion()`) to continuously update the clock display.
