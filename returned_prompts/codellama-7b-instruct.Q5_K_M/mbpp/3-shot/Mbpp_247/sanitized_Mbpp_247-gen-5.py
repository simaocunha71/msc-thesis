def lps(input_string):
  def lps_helper(left, right):
    if left >= right:
      return 0
    if input_string[left] == input_string[right]:
      return 2 + lps_helper(left + 1, right - 1)
    else:
      return max(lps_helper(left + 1, right), lps_helper(left, right - 1))
  return lps_helper(0, len(input_string) - 1)