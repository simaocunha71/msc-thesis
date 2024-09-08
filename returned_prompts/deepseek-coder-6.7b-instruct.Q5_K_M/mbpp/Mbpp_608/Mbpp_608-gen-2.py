def bell_Number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

print(bell_Number(2))

Explanation:
The bell number is a sequence of numbers of which the kth term is the sum of the numbers in the (k-1)th row of the Pascal triangle. The first few terms are 1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213557, 27644437, 190899322, 1306534161, 9148527640, 64384445401, 470846051285, 3542417059820, 27314150848187, 212282310940905, 1670442948469260, 13274268349305687, 106880768566508201, 868802126122248870, 7108110824842407757, 58350221440480255085, 481084181902004650820, 