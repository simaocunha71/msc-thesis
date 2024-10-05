
    def rounded_avg(n, m):
        if n>m: return -1
        return bin(round((sum(range(n, m+1))/len(range(n, m+1)))+0.5))[2:]