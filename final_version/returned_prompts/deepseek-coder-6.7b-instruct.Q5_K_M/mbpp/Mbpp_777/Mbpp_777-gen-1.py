
def find_sum(lst):
    non_repeated = set()
    repeated = set()
    for num in lst:
        if num not in non_repeated and num not in repeated:
            non_repeated.add(num)
        else:
            if num in non_repeated:
                non_repeated.remove(num)
            repeated.add(num)
    return sum(non_repeated)

print(find_sum([1,2,3,1,1,4,5,6])) # 21

Explanation:
The function works by maintaining two sets. The set `non_repeated` contains the numbers that have not been repeated in the list and the set `repeated` contains the numbers that have been repeated.

For each number in the list, if it is not in `non_repeated` and not in `repeated`, it is added to `non_repeated`.

If the number is in `non_repeated`, it is removed from `non_repeated` and added to `repeated`, because it has been repeated.

Finally, the function returns the sum of the numbers in `non_repeated`.

The time complexity of the function is O(n), where n is the length of the list, because it iterates through the list once. The space complexity is also O(n) because the function uses two sets to store the numbers in the list.

"""

