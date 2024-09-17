
def maxAverageOfPath(arr):
  total = 0
  for row in arr:
    for num in row:
      total += num

  n = len(arr) * len(arr[0])
  average = total / n

  max_average = average
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      total -= arr[i][j]
      average = total / (n - 1)
      max_average = max(max_average, average)
      total += arr[i][j]

  return max_average


