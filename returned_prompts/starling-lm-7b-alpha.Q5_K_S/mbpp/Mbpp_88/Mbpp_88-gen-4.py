def freq_count(lst):
    dct={}
    for i in lst:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct


# def freq_count(lst):
#     dct={}
#     for i in lst:
#         if i not in dct:
#             dct[i]=1
#         else:
#             dct[i]+=1
#     return dct


# def freq_count(lst):
#     dct={}
#     for i in lst:
#         dct[i]=dct.get(i,0)+1
#     return dct

# def freq_count(lst):
#     return dict.fromkeys(lst,0).fromkeys(lst,1)


# def freq_count(lst):
#     dct={}
#     for i in lst:
#         if i in dct:
#             dct[i]+=1
#         else:
#             dct[i]=1
#     return dct

"""
def freq_count(lst):
    dct={}
    for i in lst:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct
"""


"""
def freq_count(lst):
    dct={}
    for i in lst:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct
"""

# def freq_count(lst):
#     dct={}
#     for i in lst:
#         if i not in dct:
#             dct[i]=0
#         dct[i]+=1
#     return dct

# def freq_count(lst):
#     dct={}
#     for i in lst:
#         if i in dct:
#             dct[i]+=1
#         else: