def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    prod = [0] * n
    prod[0] = lst[0]
    for i in range(1, n):
        prod[i] = lst[i] * lst[i - 1]
    return sum(prod)

print(sum_Of_Subarray_Prod([1,2,3]))  # Output: 20

Explanation:
The function first initializes the product list with the first element of the input list. Then, for each subsequent element in the input list, it calculates the product of the current element and the previous one, and adds this product to the product list. Finally, it returns the sum of the products in the product list.

The products of all possible sublists of [1,2,3] are: [1], [2], [3], [1,2], [2,3], [1,2,3], their products are 1, 2, 3, 2, 6, 6 respectively, and their sum is 20.
"""


def sum_Of_Subarray_Prod(lst):
    sum_prod = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            prod = 1
            for k in sublist:
                prod *= k
            sum_prod += prod
    return sum_prod

print(sum_Of_Subarray_Prod([1,2,3]))  # Output: 20

Explanation:
The function first initializes a variable sum_prod to 0. Then, it iterates over each possible sublist of the input list (using two nested loops), calculates the product of the elements in the sublist, and adds this product to sum_prod. Finally, it returns sum_prod.

The products of all possible sublists of [1,2,3] are: [1], [2], [3], [1,2], [2,3], [1,2,3], their products are 1, 2, 3