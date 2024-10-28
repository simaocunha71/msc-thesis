    if n%2!=0{
        return false
    }

    for i:=1; i<=n/2; i++{
        for j:=i; j<=n/2; j++{
            for k:=j; k<=n/2; k++{
                for l:=k; l<=n/2; l++{
                    if i+j+k+l==n{
                        return true
                    }
                }
            }
        }
    }

    return false
}



