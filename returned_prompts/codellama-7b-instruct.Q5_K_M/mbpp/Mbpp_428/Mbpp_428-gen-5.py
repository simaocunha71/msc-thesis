
def shell_sort(arr):
  n = len(arr)

  # Start with a big gap, then reduce the gap
  for gap in range(n//2, 0, -1):
    # Do a gapped insertion sort for this gap size.
    # The first gap elements are already in gapped order
    # keep track of the maximum value in the gapped sorted array.
    max_in_gap = 0

    # Compare all elements in the gap with the previous gap elements.
    for i in range(gap, n):
      current_value = arr[i]
      position = i

      # if current_value > arr[i - gap]:
      # Swap the unsorted element with the previous gap elements.
      while position >= gap and current_value < arr[position - gap]:
        arr[position] = arr[position - gap]
        position -= gap

      # Put the element in its correct position.
      arr[position] = current_value

      # Update the maximum value in the gap
      max_in_gap = max(max_in_gap, arr[position])

  return arr


