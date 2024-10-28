def sum_list(a,b):
    """
    takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
    """
    if len(a)!=len(b):
        return False
    if len(a)==0:
        return []
    res=[]
    for i in range(len(a)):
        res.append(a[i]+b[i])
    return res