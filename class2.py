import numpy as np
import csv
import plotly.express as px

def plotgraph(data_path):
    with open(data_path)as csv_file:
        df = csv.DictReader(csv_file)
        graph = px.scatter(df, x = 'TV Size', y ='Time Spent')
        graph.show()

def getDataSource(data_path):
    size = []
    time = []

    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for i in csv_reader:
            size.append(float(i['TV Size']))
            time.append(float(i['Time Spent']))
    
    return {'x' : size, 'y' : time}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])

    print('Correlation of Size vs. Time : ', correlation[0, 1])

def setup():
    data_path = 'class2.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotgraph(data_path)

setup()