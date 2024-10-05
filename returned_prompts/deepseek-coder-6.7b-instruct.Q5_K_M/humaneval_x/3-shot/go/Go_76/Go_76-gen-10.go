    if x ==1{
        return true
    }
    if n<2{
        return false
    }
    for i:=2;i*i<=x;i++{
        if math.Mod(float64(x),float64(i))==0{
            for x%i==0{
                x/=i
                if x==1{
                    return true
                }
            }
        }
    }
    return false
}



