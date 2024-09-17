
def toggle_middle_bits(n):
  first = n & 1
  last = n & 2
  middle = n >> 1
  toggle = ~middle
  result = first + last + toggle
  return result


