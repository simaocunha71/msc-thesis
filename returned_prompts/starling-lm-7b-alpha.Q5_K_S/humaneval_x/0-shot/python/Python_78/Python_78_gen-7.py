
def hex_key(num):
    hex_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    result = 0
    for i in num:
        if hex_dict[i] in [2,3,5,7,11,13]:
            result += 1
    return result


# def hex_key(num):
#     hex_dict = {str(i):i for i in range(16)}
#     hex_dict['A'] = 10
#     hex_dict['B'] = 11
#     hex_dict['C'] = 12
#     hex_dict['D'] = 13
#     hex_dict['E'] = 14
#     hex_dict['F'] = 15
#     hex_key = []
#     for i in num:
#         hex_key.append(hex_dict[i])
#     result = 0
#     for i in hex_key:
#         if i in [2,3,5,7,11,13]:
#             result += 1
#     return result


# def hex_key(num):
#     hex_dict = {str(i):i for i in range(16)}
#     hex_dict['A'] = 10
#     hex_dict['B'] = 11
#     hex_dict['C'] = 12
#     hex_dict['D'] = 13
#     hex_dict['E'] = 14
#     hex_dict['F'] = 15
#     hex_key = []
#     for i in num:
#         hex_key.append(hex_dict[i])
#     result = 0
#     for i in hex_key:
#         if i in [2,3,5,7,11,13]:
#             result +=