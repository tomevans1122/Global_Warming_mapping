import requests
import bs4
import numpy as np
import matplotlib.pyplot as plt

result = requests.get("https://www.trevorharley.com/hottest-day-of-each-year-from-1900.html")
soup = bs4.BeautifulSoup(result.text, "lxml")


all_temps_lst = []
i = 1
while i < 120:
    x = soup.select('p')[i].getText()
    val = float(x[5:9])
    all_temps_lst.append(val)
    i += 1
    continue

all_temps_array = np.array(all_temps_lst)
years = np.arange(0, 119, 1)


def straight_line_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    line = m * x + b
    return line


best_fit = straight_line_fit(years, all_temps_array)

plt.grid(True)
plt.plot(years, all_temps_array, 'o', color='black')
plt.plot(years, best_fit, 'r--')
plt.title("Highest Temperature Measured in UK over 119 years")
plt.xlabel("Years from 1900 to 2019")
plt.ylabel("Temperature (\u00B0C)")
plt.show()