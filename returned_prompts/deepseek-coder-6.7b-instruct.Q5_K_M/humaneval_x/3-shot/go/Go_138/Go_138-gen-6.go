    if n%2 != 0{
        return false
    }
    for i:=2; i<n; i+=2{
        for j:=i+2; j<n; j+=2{
            for k:=j+2; k<n; k+=2{
                for l:=k+2; l<=n; l+=2{
                    if i+j+k+l == n{
                        return true
                    }
                }
            }
        }
    }
    return false
}



