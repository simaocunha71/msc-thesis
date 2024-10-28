# Code here
def sum_squares(lst):
    upper = []
    for i in lst:
        upper.append(int(i) + 0.9999)
    sum_square = 0
    for i in upper:
        sum_square += i ** 2
    return sum_square




#lst = input().split(',')
lst = [1.4,4.2,0]
print(sum_squares(lst))





#lst = input().split(',')
#print(sum_squares(lst))

```