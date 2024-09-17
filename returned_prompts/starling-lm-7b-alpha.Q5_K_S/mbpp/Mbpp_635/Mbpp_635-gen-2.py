
def heap_sort(nums: list) -> list:
  n = len(nums)
  for i in range(n//2 - 1, -1, -1):
    heapify(nums, n, i)
  for i in range(n-1, 0, -1):
    nums[i], nums[0] = nums[0], nums[i]
    heapify(nums, i, 0)
  return nums

def heapify(nums: list, n: int, i: int) -> None:
  left = 2 * i + 1
  right = 2 * i + 2
  largest = i
  if left < n and nums[i] < nums[left]:
    largest = left
  if right < n and nums[largest] < nums[right]:
    largest = right
  if largest != i:
    nums[i], nums[largest] = nums[largest], nums[i]
    heapify(nums, n, largest)


