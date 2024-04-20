"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def sum(n):
    if n < 3: # if the number is less than three just return it as is since it has already been calculated earlier
        return n
    else: # otherwise calculate the total sum of the numbers below and above given value
        total_sum = (n - cal_sum(n-1)) + cal_sum(n+1)
        return total_sum
print('The sum of all Perrin Numbers is ', end='')
for i in range(3, 50):
    print(f'{i:>2}', end = ' ')
    print()
print('The sum of all Perrin Numbers is ', end='')
for i in range(17,34) :
    print(f'{i:>2}',end= '')
    print()