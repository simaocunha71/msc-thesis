
def find_Odd_Pair(nums, k):
  return len([i for i in nums if bin(i^k).count("1")%2])


