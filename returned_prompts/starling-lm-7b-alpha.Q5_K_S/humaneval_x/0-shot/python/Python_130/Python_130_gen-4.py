
def tri(n):
    result = []
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 3]
    else:
        result.append(1)
        result.append(3)
        for _ in range(3, n + 1):
            if _ % 2 == 0:
                result.append(3)
            else:
                result.append(result[-1] + result[-2] + result[-3])
    return result

# def tri(n):
#     result = [1, 3]
#     if n == 0:
#         return []
#     elif n == 1:
#         return result
#     elif n == 2:
#         return result + [2]
#     else:
#         for _ in range(3, n + 1):
#             if _ % 2 == 0:
#                 result.append(3)
#             else:
#                 result.append(result[-1] + result[-2] + result[-3])
#         return result


# Made By Mostafa_Khaled
```
     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓


        



        




```

```