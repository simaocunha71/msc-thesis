
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)


print(solution([5, 8, 7, 1]))  #==> 应返回 12
print(solution([3, 3, 3, 3, 3]))  #==> 应返回 9
print(solution([30, 13, 24, 321]))  #==> 应返回 0

在上面的代码中，我们使用了一个生成器表达式来生成列表中每隔一个元素（使用步长为2），然后我们检查这个元素是否为奇数（通过取模运算）。如果是奇数，则将其加到总和中。

这种方法的时间复杂度是O(n)，因为我们只对列表进行一次迭代。它还使用了内置的sum函数，它的时间复杂度也是O(n)。因此，该解决方案的总时间复杂度是O(n)。

注意：在Python中，索引从0开始，所以在这种情况下，我们从第一个元素开始（索引为0），然后选择每隔一个元素。
"""


def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 应返回 12
    solution([3, 3, 3, 3, 3]) ==> 应返回 9
    solution([30, 13, 24, 321]) ==> 应返回 0
    """

    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)


print(solution([5, 8, 7, 1]))  #==> 应返回 12
print(solution([3, 3, 3