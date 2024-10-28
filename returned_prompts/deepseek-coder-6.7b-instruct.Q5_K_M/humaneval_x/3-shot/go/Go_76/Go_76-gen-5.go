    if x==1{
        return true
    }

    for i:=2;i*i<=x;i++{
        if math.Mod(math.Log(float64(x))/math.Log(float64(i)),float64(n))==0{
            return true
        }
    }
    return false
}



