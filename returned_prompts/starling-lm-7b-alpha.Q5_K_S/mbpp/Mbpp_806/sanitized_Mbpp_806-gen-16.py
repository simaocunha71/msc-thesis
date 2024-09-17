def max_run_uppercase(string):
    counter = 0
    max_run = 0
    for i in range(len(string)):
        if string[i].isupper():
            counter += 1
        else:
            counter = 0
        max_run = max(max_run, counter)
    return max_run