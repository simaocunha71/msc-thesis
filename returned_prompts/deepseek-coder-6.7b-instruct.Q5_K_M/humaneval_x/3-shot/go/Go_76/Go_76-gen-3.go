    if x==1{
        return true
    }
    for i:=2;i<=x/2;i++{
        if math.Pow(float64(n),float64(i))==float64(x){
            return true
        }
    }
    return false
}



