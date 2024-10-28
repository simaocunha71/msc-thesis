
def maxAverageOfPath(arr: list[list[int]]) -> float:
  def sumOfPath(arr: list[list[int]], row: int, col: int) -> int:
    sum = 0
    while row < len(arr) and col < len(arr[0]):
      sum += arr[row][col]
      row += 1
      col += 1
    return sum

  maxAverage = -1
  for row in range(len(arr)):
    for col in range(len(arr[0])):
      pathSum = sumOfPath(arr, row, col)
      average = pathSum / (len(arr) + len(arr[0]) - 2)
      maxAverage = max(maxAverage, average)
  return maxAverage


