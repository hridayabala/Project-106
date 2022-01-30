import numpy as np
import csv
import plotly.express as px

def plotgraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        graph = px.scatter(df, x = 'Temperature', y = 'Ice-cream Sales')
        graph.show()

def getDataSource(data_path):
    ics = []
    cds = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for i in csv_reader:
            ics.append(float(i['Temperature']))
            cds.append(float(i['Ice-cream Sales']))
    
    return {'x' : ics, 'y' : cds}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    
    print('Correlation of Temperature vs. Ice-cream Sales : ', correlation[0, 1])

def setup():
    data_path = 'class1.csv'
    data_source = getDataSource(data_path)

    findCorrelation(data_source)

    plotgraph(data_path)

setup()