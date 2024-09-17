def find_kth(nums1: list, nums2: list, k: int) -> int:
  m, n = len(nums1), len(nums2)
  i = j = 0
  while True:
    if i == m:
      return nums2[j+k-1]
    if j == n:
      return nums1[i+k-1]
    if k == 1:
      return min(nums1[i], nums2[j])
    ni = min(i+k//2, m)
    nj = min(j+k//2, n)
    pi = nums1[ni-1]
    pj = nums2[nj-1]
    if pi > pj:
      k -= ni-i
      i = ni
    else:
      k -= nj-j
      j = nj