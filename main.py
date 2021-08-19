from pandas.core.reshape.reshape import stack_multiple
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("medium.csv")
data=df["reading_time"].to_list()

fig=ff.create_distplot([data],["Reading Time"],show_hist=False)
fig.show()

pop_mean=statistics.mean(data)
pop_std=statistics.stdev(data)
print("Mean of the population: ",pop_mean)
print("Standard Deviation of the population: ",pop_std)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list,mean,sd):
    df=mean_list
    sd1_start,sd1_end=mean-sd,mean+sd
    sd2_start,sd2_end=mean-(2*sd),mean+(2*sd)
    sd3_start,sd3_end=mean-(3*sd),mean+(3*sd)

    fig=ff.create_distplot([df],["Reading Time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.add_trace(go.Scatter(x=[sd1_start,sd1_start],y=[0,1],mode="lines",name="SD1 Start"))
    fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,1],mode="lines",name="SD1 End"))
    fig.add_trace(go.Scatter(x=[sd2_start,sd2_start],y=[0,1],mode="lines",name="SD2 Start"))
    fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,1],mode="lines",name="SD2 End"))
    fig.add_trace(go.Scatter(x=[sd3_start,sd3_start],y=[0,1],mode="lines",name="SD3 Start"))
    fig.add_trace(go.Scatter(x=[sd3_end,sd3_end],y=[0,1],mode="lines",name="SD3 End"))
    fig.show()

    z_score=(statistics.mean(data)-mean)/sd
    print("The Z-Score: ",z_score)

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)

    sam_mean=statistics.mean(mean_list)
    sam_std=statistics.stdev(mean_list)
    print("\nMean of sampling: ",sam_mean)
    print("Standard Deviation of sampling: ",sam_std)
    show_fig(mean_list,sam_mean,sam_std)

setup()