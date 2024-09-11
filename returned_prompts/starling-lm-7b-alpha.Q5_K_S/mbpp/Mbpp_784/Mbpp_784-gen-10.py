def mul_even_odd(num_list):
    even, odd = [], []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0:
        return 0
    elif len(odd) == 0:
        return even[0]
    else:
        return even[0] * odd[0]



if __name__ == "__main__":
    print(mul_even_odd([1,3,5,7,4,1,6,8]))




"""
Even Numbers: [2, 4, 6, 8]
Odd Numbers: [1, 3, 5, 7]

Even Numbers: [2, 4, 6, 8]
Odd Numbers: [3, 5, 7]

Even Numbers: [2, 4, 6, 8]
Odd Numbers: [5, 7]

Even Numbers: [2, 4, 6, 8]
Odd Numbers: [7]

Even Numbers: [2, 4, 6, 8]
Odd Numbers: [8]

Even Numbers: [2, 4, 6, 8]
Odd Numbers: []

Even Numbers: [4, 6, 8]
Odd Numbers: []

Even Numbers: [4, 6, 8]
Odd Numbers: [1]
"""







"""
def mul_even_odd(num_list):
    even, odd = [], []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0:
        return 0
    elif len(odd) == 0:
        return even[0]
    else:
        return even[0] * odd[0]

assert mul_even_odd([1,3,5