import csv
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = 'data/sitka_weather_2018_simple.csv'

with open(FILENAME) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # Get dates, highs and lows from the file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the highs and lows
    plt.style.use(style='default')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    ax.set_title('Daily highs and lows temperatures - 2018', fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('img/sitka_highs_lows_temperature.png', bbox_inches='tight')