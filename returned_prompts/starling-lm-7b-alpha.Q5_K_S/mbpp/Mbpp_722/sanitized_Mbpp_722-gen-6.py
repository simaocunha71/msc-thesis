def filter_data(data,height,weight):
    result={}
    for key,value in data.items():
        if value[0]>height and value[1]>weight:
            result[key]=value
    return result