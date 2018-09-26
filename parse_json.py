import json
from pprint import pprint
from plot import plot_drive
import os


def parse_plot():
    plots = {}
    for file in os.listdir('data'):
        filename = os.fsdecode(file)
        if filename.endswith(".chlsj"):
            file = open("data/" + filename, "r")
            data = json.load(file)
            plots[filename] = {}
            x = []
            y = []

            for i in range(len(data)):
                # pprint(data[i]['durations']['total']) # 954290681
                if "fox" in data[i]['host'] and data[i]['durations']['response'] is not None and data[i]['durations']['response'] < 100000:  # to remove one big outlier
                    x.append(data[i]['durations']['response'])
                    y.append(data[i]['durations']['total'])

            plots[filename]['x'] = x
            plots[filename]['y'] = y
    pprint(data[3])
    # plot_drive(plots)

    '''
    Plots
    SVM PCA full math
    Potential Data points
        Status: 5xx, 4xx?
    algorithm implement / param tuning SVM 1 class
    
    '''


parse_plot()

