    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), -nums.index(x)))  # Sort by sum of digits and index in reverse order.  # noqa: E501


