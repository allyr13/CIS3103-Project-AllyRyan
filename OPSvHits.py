# Load matplotlib.pyplot, pandas, and numpy
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load oldfaithful.csv data
def getFiles(folderPath):
    # For loop through each data file in "Data" folder
    path = folderPath
    dir_list = os.listdir(path) 
    return dir_list

dir_list = getFiles('./Data')
for item in dir_list:
    df = pd.read_csv("./Data/" + item)
    # Create title, font size set to 20
    plt.title('2000-2023 WS Champions', fontsize=20)
    # Create label for x-axis, font size set to 14
    plt.xlabel('OPS', fontsize=14)
    # Create label for y-axis, font size set to 14
    plt.ylabel('Hits', fontsize=14)

    plt.scatter(df['OPS'], df['H'])


plt.legend()
plt.show()
plt.savefig('OPSvsHits')
