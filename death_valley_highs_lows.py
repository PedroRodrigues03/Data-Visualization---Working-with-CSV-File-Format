import csv
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = 'data/death_valley_2018_simple.csv'

with open(FILENAME) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low =  int(row[5])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.style.use(style='default')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title('Daily highs and lows - 2018\nDeath Valley, CA', fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('img/death_valley_highs_lows.png', bbox_inches='tight')
