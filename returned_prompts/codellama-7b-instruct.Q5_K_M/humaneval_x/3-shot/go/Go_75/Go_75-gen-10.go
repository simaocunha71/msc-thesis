    for i:=2;i<100;i++{
        if a%i==0{
            for j:=2;j<100;j++{
                if a%j==0{
                    for k:=2;k<100;k++{
                        if a%k==0{
                            if i*j*k==a{
                                return true
                            }
                        }
                    }
                }
            }
        }
    }
    return false
}



