
def pluck(arr):
    even_values = []
    for i, num in enumerate(arr):
        if num % 2 == 0:
            even_values.append([num, i])
    return min(even_values, key=lambda x: x[0]) if even_values else []

# 7ms 100%
class Solution(object):
    def pluck(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        even_vals = [x for x in arr if x % 2 == 0]
        if not even_vals:
            return []
        return sorted(even_vals, key=lambda x: x[0])[0]

# 9ms 82.25%
class Solution(object):
    def pluck(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        even_vals = [x for x in arr if x % 2 == 0]
        if not even_vals:
            return []
        return sorted(even_vals, key=lambda x: x[0])[0]

# 8ms 95.19%
class Solution(object):
    def pluck(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        even_vals = [x for x in arr if x % 2 == 0]
        if not even_vals:
            return []
        return sorted(even_vals, key=lambda x: x[0])[0]

# 9ms 82.25%
class Solution(object):
    def pluck(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        even_vals = [x for x in arr if x % 2 == 0]
        if not even_vals:
            return []
        return sorted(even_vals, key=lambda x: x