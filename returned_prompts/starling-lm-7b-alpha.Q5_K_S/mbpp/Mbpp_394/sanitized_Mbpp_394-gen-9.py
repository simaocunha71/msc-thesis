def check_distinct(t):
    # Convert tuple to set and compare length
    if(len(t) == len(set(t))):
        return True
    else:
        return False