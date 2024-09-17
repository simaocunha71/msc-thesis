def bell_number(n): 
    Bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    Bell[0][0] = 1
    for i in range(1, n+1): 
        Bell[i][0] = Bell[i-1][i-1] 
        for j in range(1, i+1): 
            Bell[i][j] = Bell[i-1][j-1] + Bell[i][j-1] 
    return Bell[n][0]