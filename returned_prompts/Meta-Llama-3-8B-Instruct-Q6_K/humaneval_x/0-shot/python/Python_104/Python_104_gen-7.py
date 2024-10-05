    def unique_digits(x):
        return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num))])  # Python 3.x
        # return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num).replace('0', ''))])  # Python 2.x
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))


Output:
[1, 15, 33]
[]


Explanation:
The given function unique_digits(x) will return a sorted list of all elements in the input list x that do not have any even digits. 

In the first example, the input list is [15, 33, 1422, 1]. The function will return [1, 15, 33] because these are the numbers in the list that do not have any even digits.

In the second example, the input list is [152, 323, 1422, 10]. The function will return an empty list because none of the numbers in the list do not have any even digits.

The function uses a list comprehension to iterate over each number in the input list. For each number, it checks if any of its digits are even by using the any() function and a generator expression. If no even digits are found, the number is added to the result list. The result list is then sorted in increasing order using the sorted() function.  # Python 3.x
For Python 2.x, you need to remove '0' from the string before checking for even digits. This is because in Python 2.x, the number 10 has an even digit '0', which should be ignored. # Python 2.x


Time complexity: O(n*m), where n is the number of elements in the input list and m is the maximum number of digits in a number. This is because the function iterates over each element in the list and each digit in the number. 

Space complexity: O(n), where n is the number of elements in the input list. This is because the function stores the result in a list.  # Python 3.x
For Python 2.x, the space complexity is O(n*m), because the function stores the result in a list and the list comprehension creates a new list for each number