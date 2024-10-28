def filter_data(dictionary,min_height,min_weight):
    res={}
    for i in dictionary:
        if dictionary[i][0]>min_height and dictionary[i][1]>min_weight:
            res[i]=dictionary[i]
    return res