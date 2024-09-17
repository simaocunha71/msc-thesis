def count_charac(string):
    cnt = 0
    for i in range(len(string)):
        if string[i]!= " ":
            cnt+=1
    return cnt