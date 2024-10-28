def median_numbers(a,b,c):
    median = sorted([a,b,c])
    if len(median) % 2 == 0:
        return (median[len(median)-1] + median[len(median)-2])/2
    else:
        return median[len(median)-1]