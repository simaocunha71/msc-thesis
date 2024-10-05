    if n==1 || n==0 {
        return x==1
    }
    for i := 0; i < 100; i++ {
        if math.Pow(float64(n), float64(i))==float64(x) {
            return true
        }
    }
    return false
}



