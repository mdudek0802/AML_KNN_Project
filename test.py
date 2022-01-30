from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

DATASET = "2015.csv"
K_NEIGHBORS = 7

fig = plt.figure()
ax = fig.add_subplot(projection ='3d')

MARKERS = {
    0 : '$WE$',
    1 : '$NA$',
    2 : '$NZ$',
    3 : '$ME$',
    4 : '$LA$',
    5 : '$SEA$',
    6 : '$CE$',
    7 : '$EA$',
    8 : '$SSA$',
    9 : '$SA$',
}


if __name__ == "__main__":
    unique_regions = []
    region_density = []
    region_data = []
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
        temp_region_data = sub_data[sub_data["Region"] == region]
        region_density.append(len(temp_region_data))
        region_data.append(temp_region_data)

    print(region_density)
    print("Total Density: " + str(sum(region_density)))
    print(region_data)
    # print(data)
    # print()

    i = 0
    for region in region_data:
        print(MARKERS.get(i))
        print(region)
        # ax.scatter(region["Happiness Score"], region["Economy (GDP per Capita)"], range(0,len(region)), marker=MARKERS.get(i))
        ax.scatter(region["Happiness Score"], region["Economy (GDP per Capita)"], range(0,len(region)))
        i+=1

    # ax.plot3D(sub_data["Happiness Score"], sub_data["Economy (GDP per Capita)"], range(0,sum(region_density)), 'green')

    # ax.scatter3D(sub_data["Happiness Score"], sub_data["Economy (GDP per Capita)"], range(0,sum(region_density)), c=range(0,sum(region_density)), cmap='Blues')
    plt.show()


