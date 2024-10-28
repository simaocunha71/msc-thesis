    for i:=1; i < n; i++ {
        for j:=i+1; j < n; j++ {
            for k:=j+1; k < n; k++ {
                for l:=k+1; l < n; l++ {
                    if i + j + k + l == n && i % 2 == 0 && j % 2 == 0 && k % 2 == 0 && l % 2 == 0 {
                        return true
                    }
                }
            }
        }
    }
    return false
}



