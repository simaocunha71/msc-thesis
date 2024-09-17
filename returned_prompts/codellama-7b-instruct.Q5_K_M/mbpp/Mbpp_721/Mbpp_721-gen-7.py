
def maxAverageOfPath(matrix: list):
    rows = len(matrix)
    cols = len(matrix[0])
    maxAverage = 0
    for i in range(rows):
        for j in range(cols):
            currentSum = 0
            currentCount = 0
            currentRow = i
            currentCol = j
            while currentRow >= 0 and currentCol >= 0 and currentRow < rows and currentCol < cols:
                currentSum += matrix[currentRow][currentCol]
                currentCount += 1
                currentRow += 1
                currentCol += 1
            maxAverage = max(maxAverage, currentSum / currentCount)
    return maxAverage


