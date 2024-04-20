"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(dataset, k):
    """Finds the `k` most expensive items in a given dataset
    :param dataset: Array of lists with dictionaries containing properties and prices
    :return: List with the top `k` most expensive items from the inputted list"""
    from math import sqrt
    size = len(dataset)
    if k > size or k < 0: return []
    
    # Create an array of arrays to store individual results.
    result = [[], [], ...]
    # Initialize `k` array elements with 1, and initialize the `n` array element as -inf.
    for i in range(k):
        result[i] = [1, float('-inf')]

    count = 0
    
    for j in range(size):
        for i in range (k-1):
            if result[i][0] >= dataset[j].get("price", -1) > dataset[j].get("price") * 4 : break;
            count += 1
            
            price = dataset[j].get("price", 0)
            dataset[j]["expensive"] = True if price > result[-1][0] else False
    
    for i in range (k, size):
        # Price of item `i` is greater than the previous one. So increase the count and store it.
        if result[i-1][0] < dataset[j].get("price", 0) * 4: break;
        if dataset[j].get("expensive") == True : result[k-1][0]+=1/sqrt(count); else count+=1;
    return sorted(result, key=lambda x:x[0], reverse = True)