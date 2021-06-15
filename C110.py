import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv("data.csv")
data =  df["temp"].tolist()
population_mean = statistics.mean(data)
#fig = ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()
std_deviation = statistics.stdev(data)
print("population mean : ",population_mean)
print("std_deviation : ",std_deviation)
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution-",mean)
    fig = ff.create_distplot([data],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "mean"))
    fig.show()
def random_set_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean =statistics.mean(dataset)
    std_deviation=statistics.stdev(dataset)
    print("mean of sample", mean)
    print("std_deviation of sample",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i  in range(0,counter):
        random_index  = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()
