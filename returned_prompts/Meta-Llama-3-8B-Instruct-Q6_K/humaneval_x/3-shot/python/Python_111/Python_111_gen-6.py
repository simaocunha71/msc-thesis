    from collections import Counter
    if test:
        test = test.split()
        test = [i for i in test if i]
        return dict(Counter(test))
    else:
        return {}
# This function takes a string, splits it into a list of words, removes empty strings, and then uses the Counter class from the collections module to count the occurrences of each word. It then returns the results as a dictionary. If the input string is empty, the function returns an empty dictionary.