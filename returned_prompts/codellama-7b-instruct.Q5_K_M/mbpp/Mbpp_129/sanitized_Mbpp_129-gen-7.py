def magic_square_test(matrix):
    # TODO: write your code here
    # 检查列和行是否相等
    if len(matrix)!=len(matrix[0]):
        return False
    # 检查对角线是否相等
    if matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3]!=matrix[0][3]+matrix[1][2]+matrix[2][1]+matrix[3][0]:
        return False
    # 检查每一列是否相等
    for i in range(4):
        if matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]!=matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]:
            return False
    # 检查每一行是否相等
    for i in range(4):
        if matrix[i][0]+matrix[i][1]+matrix[i][2]+matrix[i][3]!=matrix[i][0]+matrix[i][1]+matrix[i][2]+matrix[i][3]:
            return False
    # 检查数字是否相等
    for i in range(4):
        for j in range(4):
            if matrix[i][j]!=matrix[0][0]:
                return False
    return True