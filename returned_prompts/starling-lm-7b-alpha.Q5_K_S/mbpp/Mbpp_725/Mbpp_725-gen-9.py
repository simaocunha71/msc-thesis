"""
def extract_quotation(s):
    return re.findall('"(.*?)"', s)

"""

def extract_quotation(s):
    result = []
    index = 0
    while index < len(s):
        if s[index] == '"':
            start = index + 1
            index += 1
            while s[index] != '"':
                result.append(s[start:index])
                index += 1
            index += 1
        else:
            index += 1
    return result

import re

def extract_quotation(s):
    return re.findall('"(.*?)"', s)

# assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))

# def extract_quotation(s):
#     result = []
#     start = -1
#     end = -1
#     for i in range(len(s)):
#         if s[i] == '"':
#             if start == -1:
#                 start = i
#             else:
#                 end = i
#                 result.append(s[start+1:end])
#                 start = -1
#     if start != -1:
#         result.append(s[start+1:len(s)])
#     return result

# def extract_quotation(s):
#     result = []
#     index = s.find('"')
#     while index != -1:
#         start = index + 1
#         index = s.find('"', index + 1)
#         if index != -1:
#             result.append(s[start:index])
#         index = s.find('"', index + 1)
#     return result


# def extract_quotation(s):
#     result = []
#     index = 0
#     while index < len(s):
#         if s[index] == '"