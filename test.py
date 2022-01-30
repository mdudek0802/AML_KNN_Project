from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

DATASET = "2015.csv"
K_NEIGHBORS = 7

fig = plt.figure()
ax = plt.axes(projection ='3d')

if __name__ == "__main__":
    unique_regions = []
    region_density = []
    data = pd.read_csv(DATASET)
    data = pd.DataFrame(data)
    regions = data["Region"]
    for region in regions:
        if region not in unique_regions:
            unique_regions.append(region)
    
    print(len(unique_regions))
    print(unique_regions)

    sub_data = data[["Country", "Region", "Happiness Score", "Economy (GDP per Capita)",
                    "Family", "Health (Life Expectancy)", "Freedom",
                    "Trust (Government Corruption)", "Generosity"]]

    for region in unique_regions:
        region_density.append(len(sub_data[sub_data["Region"] == region]))

    print(region_density)
    print("Total Density: " + str(sum(region_density)))
    # print(data)
    # print()

    ax.plot3D(sub_data["Happiness Score"], sub_data["Economy (GDP per Capita)"], range(0,sum(region_density)), 'green')
    plt.show()


