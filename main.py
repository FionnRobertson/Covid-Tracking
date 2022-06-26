# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from tabulate import tabulate

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    raw_data = pd.read_csv("https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=hospitalCases&metric=newCasesBySpecimenDate&metric=newDeaths28DaysByDeathDate&metric=newVirusTestsBySpecimenDate&metric=newAdmissions&format=csv")
    data = raw_data[0:60]
    print(tabulate(data[0:10], headers=data.keys(), tablefmt="orgtbl"))

fig, ax = plt.subplots()

# Plot linear sequence, and set tick labels to the same color
ax.plot(data["hospitalCases"], color='red')
ax.tick_params(axis='y', labelcolor='red')

# Generate a new Axes instance, on the tw
# in-X axes (same position)
ax2 = ax.twinx()

# Plot exponential sequence, set scale to logarithmic and change tick color
ax2.plot(data["newCasesBySpecimenDate"], color='green')
ax2.tick_params(axis='y', labelcolor='green')
plt.gca().invert_xaxis()
plt.show()