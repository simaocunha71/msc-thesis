
class Solution(object):
    def find_first_occurrence(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                right = mid - 1
            elif A[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if left < len(A) and A[left] == target else -1
