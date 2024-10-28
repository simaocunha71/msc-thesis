    if x==1 {
        return true
    }
    if n==1 {
        return false
    }
    for i:=2; i<=x; i++ {
        if math.Pow(float64(n),float64(i))==float64(x) {
            return true
        }
    }
    return false
}

