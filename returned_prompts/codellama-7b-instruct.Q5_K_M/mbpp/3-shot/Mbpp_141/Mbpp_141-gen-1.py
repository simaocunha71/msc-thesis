
def pancake_sort(lst):
  for i in range(len(lst)-1, 0, -1):
    if lst[i] > lst[0]:
      flip(lst, 0, i)
      flip(lst, i, len(lst) - 1)
  return lst

def flip(lst, start, end):
  while start < end:
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1


