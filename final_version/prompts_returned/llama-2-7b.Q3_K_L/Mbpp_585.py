"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
import numpy as np
def expensive_items(dataset, k):
    sortedData = sortByPrice(dataset)
    return np.array([item for i, item in enumerate(sortedData[0:k]) if sortedData[i][1] > sortedData[-1][1]])