    if need > remaining:
        return [need + number, 0]
    else:
        return [need + number, remaining - need]  # need - number of carrots left after eating
# https://www.hackerrank.com/challenges/eat/problem
# Python 3 solution. This function takes in the number of carrots already eaten, the number of carrots needed, and the number of remaining carrots. It returns a list with the total number of eaten carrots after meals and the number of carrots left after meals. If there are not enough remaining carrots, it eats all remaining carrots and still remains hungry. The function assumes that the input values are within the given constraints (0 <= number <= 1000, 0 <= need <= 1000, 0 <= remaining <= 1000). The time complexity of this function is O(1), which means it runs in constant time. The space complexity is also O(1), which means it uses a constant amount of space.  # noqa: E501
# Test case examples:
# * eat(5, 6, 10) -> [11, 4]
# * eat(4, 8, 9) -> [12, 1]
# * eat(1, 10, 10) -> [11, 0]
# * eat(2, 11, 5) -> [7, 0]  # noqa: E501
# https://www.hackerrank.com/challenges/eat/problem
# Python 3 solution. This function takes in the number of carrots already eaten, the number of carrots needed, and the number of remaining carrots. It returns a list with the total number of eaten carrots after meals and the number of carrots left after meals. If there are not enough remaining carrots, it eats all remaining carrots and still remains hungry. The function assumes that the input values are within the given constraints (0 <= number <= 1000, 0 <= need <= 1000, 0 <= remaining <= 1000). The time complexity of this function is O(1), which means it runs in constant time. The space complexity is also O(1), which means it uses a constant amount of space.  # noqa: E501
# Test case examples:
# * eat(5, 6, 10) -> [11, 4]
# * eat(4, 8, 9) -> [12, 1]
# *