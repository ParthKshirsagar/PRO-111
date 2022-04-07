import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics as stats

df = pd.read_csv('./csv/medium_data.csv')
data = df['reading_time'].tolist()

population_mean = stats.mean(data)
population_std_dev = stats.stdev(data)
print("Population Mean: ", population_mean)
print("Population Standard Deviation: ", population_std_dev)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        dataset.append(data[random_index])
    mean = stats.mean(dataset)
    return mean

def plot_graph(mean_list):
    fig = ff.create_distplot([mean_list], ['reading_time'], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    sample_mean = stats.mean(mean_list)
    sample_std_dev = stats.stdev(mean_list)
    print("Sample Mean: ", sample_mean)
    print("Sample Standard Deviation: ", sample_std_dev)

    first_std_dev_start, first_std_dev_end = population_mean-sample_std_dev, population_mean+sample_std_dev
    second_std_dev_start, second_std_dev_end = population_mean-(2*sample_std_dev), population_mean+(2*sample_std_dev)
    third_std_dev_start, third_std_dev_end = population_mean-(3*sample_std_dev), population_mean+(3*sample_std_dev)

    sample2_df = pd.read_csv('./csv/sample_2.csv')
    sample2_data = sample2_df['reading_time'].tolist()
    sample2_mean = stats.mean(sample2_data)
    fig = ff.create_distplot([mean_list], ['Reading Time'], show_hist=False)
    fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,1], mode='lines', name='Mean'))
    fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0,1], mode='lines', name='First Standard Deviation Start'))
    fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0,1], mode='lines', name='First Standard Deviation End'))
    fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0,1], mode='lines', name='Second Standard Deviation Start'))
    fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0,1], mode='lines', name='Second Standard Deviation End'))
    fig.add_trace(go.Scatter(x=[sample2_mean, sample2_mean], y=[0,1], mode='lines', name='Sample Data Mean'))
    fig.show()

    z_score = (sample_mean-sample2_mean)/sample_std_dev
    print("Z-Score of Sample 2 Data is: ", z_score)

setup()