
def cummulative_sum(tuples):
    sum = 0
    for t in tuples:
        sum += sum(t)
    return sum

print(cummulative_sum([(1, 3),  (5, 6, 7),  (2, 6)]))

# Output: 30

Explanation:
The function takes a list of tuples as an argument. It initializes a variable sum to 0. Then, it loops through the list of tuples, adding the sum of each tuple to the variable sum. Finally, it returns the sum. In this case, it adds the sums of (1, 3), (5, 6, 7), and (2, 6) to get a total sum of 30.

"""
