
def check_distinct(t):
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            if t[i] == t[j]:
                return False
    return True


