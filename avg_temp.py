import numpy as np
import matplotlib.pyplot as plt
import json


# Reads the initial file
with open('0944b27324c5c53427812a18f045f0fa.json', 'r') as f:
    json_text = f.read()

# Decode the JSON string into a Python dictionary.
histData_dict = json.loads(json_text)


def avg_annual_temp_weekly(a, b):           # a - choose initial week, b - upper limit (hours in a year)
    test_lst = []
    while a < b:
        test_lst.append(histData_dict[a]['main']['temp'])
        a += 168                            # 168 hours in a week
        continue
    test_array = np.array(test_lst)         # test list into array
    avg = sum(test_array)/len(test_array)   # average for array
    return avg


def annual_temp_for_all_years():            # iterates through every year
    avg_yearly_lst = []
    i = 0
    j = 8760
    while j < 350664:
        avg_yearly_lst.append(avg_annual_temp_weekly(i, j))
        i += 8760
        j += 8760
        continue
    return avg_yearly_lst


def straight_line_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    line = m * x + b
    return line


def prediction_line_fit(x):                     # utilises gradient and intersection point of polyfit function
    prediction = (0.01474717689121748 * x) + 8.845128163828806
    return prediction


annual_avg_temp_array = np.array(annual_temp_for_all_years())   # array for temps
years_array = np.arange(0, 40, 1)                               # array for years
future_years_arrays = np.arange(39, 101, 1)                     # array for future years (prediction)


best_fit = straight_line_fit(years_array, annual_avg_temp_array)
prediction_line = prediction_line_fit(future_years_arrays)


# Organising the figure
plt.grid(True)
plt.plot(years_array, annual_avg_temp_array, 'o', color='black')
plt.plot(years_array, best_fit, 'r--')
plt.plot(future_years_arrays, prediction_line, 'r--')
plt.title("Average Annual Temperature Change")
plt.xlabel("Years elapsed since 1981")
plt.ylabel("Temperature (\u00B0C)")
plt.show()

