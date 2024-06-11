from datetime import datetime
from database import MongoDB
import pandas as pd

base = MongoDB()


fork = {
    'month': 'MS',
    'day': 'D',
    'hour': 'h'       
    }



def get_labels(dt_from, dt_upto, group_type):

    step = fork[group_type]
    dt_from = datetime.strptime(dt_from, '%Y-%m-%dT%H:%M:%S')
    dt_upto = datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S')
    mydates = pd.date_range(start=dt_from, end=dt_upto, freq=step).tolist()
    mydates = list(map(lambda x: x.strftime('%Y-%m-%dT%H:%M:%S'), mydates))
    return mydates

def get_total_sum(dt, group_type):
    step = fork[group_type]
    dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
    start, end = pd.date_range(start=dt, freq=step, periods=2).tolist()
    data = base.get_data(start, end)
    total = sum(map(lambda x: x['value'], data))
    return total 

def get_dataset_labels(dt_from, dt_upto, group_type):
    labels = get_labels(dt_from, dt_upto, group_type)
    dataset = []
    for x in labels:
        dataset.append(get_total_sum(x, group_type))
    return {
        'dataset': dataset,
        'labels' : labels,
    }
