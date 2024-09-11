from collections import Counter
def max_occurrences(lst):
    return max(Counter(lst).values())  # Returns the maximum frequency
    # If you want to get the item with the maximum frequency, you can use a dictionary comprehension
    # return [k for k, v in Counter(lst).items() if v == max(Counter(lst).values())][0]
    # This will return the first item that has the maximum frequency, if there are multiple items with the same maximum frequency, it will return the first one. 
    # If you want to get all items with the maximum frequency, you can use a list comprehension
    # return [k for k, v in Counter(lst).items() if v == max(Counter(lst).values())] 
    # This will return all items that have the maximum frequency.  # Returns the item with the maximum frequency
    # If you want to get the item with the maximum frequency and its frequency, you can use a dictionary comprehension
    # return [(k, v) for k, v in Counter(lst).items() if v == max(Counter(lst).values())][0]  # Returns the item with the maximum frequency and its frequency
    # This will return the first item that has the maximum frequency, if there are multiple items with the same maximum frequency, it will return the first one. 
    # If you want to get all items with the maximum frequency and their frequencies, you can use a list comprehension
    # return [(k, v) for k, v in Counter(lst).items() if v == max(Counter(lst).values())]  # Returns the item with the maximum frequency and its frequency
    # This will return all items that have the maximum frequency.  # Returns the item with the maximum frequency
    # If you want to get the item with the maximum frequency and its frequency, you can use a dictionary comprehension
    # return [(k, v) for k, v in Counter(lst).items() if v == max(Counter(lst).values())][0]  # Returns the item with the maximum frequency and its frequency
    # This will return the first item that has the maximum frequency, if there are multiple items with the same maximum frequency, it will return the first one. 
    # If you want to get all items with the maximum frequency and their frequencies, you can use a list comprehension
    # return [(k, v) for k, v in Counter(lst).items