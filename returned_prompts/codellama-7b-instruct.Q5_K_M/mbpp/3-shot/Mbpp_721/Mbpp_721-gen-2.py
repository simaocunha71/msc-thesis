
def maxAverageOfPath(matrix):
    max_avg = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = 0
            count = 0
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    sum += matrix[k][l]
                    count += 1
            max_avg = max(max_avg, sum/count)
    return max_avg


