from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

DATASET = "2015.csv"
K_NEIGHBORS = 7

def plot_by_three_attributes(regions, attrib_1, attrib_2, attrib_3):
    fig = plt.figure()
    ax = fig.add_subplot(projection ='3d')
    i = 0
    for region in regions:
        ax.scatter(region[attrib_1], region[attrib_2], region[attrib_3])
        i+=1

    plt.xlabel(attrib_1)
    plt.ylabel(attrib_2)
    ax.set_zlabel(attrib_3)
    ax.legend(unique_regions, ncol=2, fontsize='small')
    plt.title(attrib_1 + " vs " + attrib_2 + " vs " + attrib_3)

    plt.show()

def plot_by_two_attributes(regions, attrib_1, attrib_2):
    fig = plt.figure()
    ax = fig.add_subplot()
    i = 0
    for region in regions:
        ax.scatter(region[attrib_1], region[attrib_2])
        i+=1

    ax.legend(unique_regions, ncol=2, fontsize='small')
    plt.xlabel(attrib_1)
    plt.ylabel(attrib_2)
    plt.title(attrib_1 + " vs " + attrib_2)

    plt.show()

if __name__ == "__main__":
    unique_regions = []
    region_density = []
    region_data = []
    data = pd.read_csv(DATASET)
    data = pd.DataFrame(data)
    regions = data["Region"]
    for region in regions:
        if region not in unique_regions and (region != 'North America' or region != 'Australia and New Zealand'):
            unique_regions.append(region)
    
    print(len(unique_regions))
    print(unique_regions)

    sub_data = data[["Country", "Region", "Happiness Score", "Economy (GDP per Capita)",
                    "Family", "Health (Life Expectancy)", "Freedom",
                    "Trust (Government Corruption)", "Generosity"]]

    for region in unique_regions:
        temp_region_data = sub_data[sub_data["Region"] == region]
        if len(temp_region_data) <= 5:
            continue
        region_density.append(len(temp_region_data))
        region_data.append(temp_region_data)

    plot_by_three_attributes(region_data, "Happiness Score", "Economy (GDP per Capita)", "Health (Life Expectancy)")
    # plot_by_two_attributes(region_data, "Happiness Score", "Economy (GDP per Capita)")


