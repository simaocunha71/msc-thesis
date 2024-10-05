    if x == 1 || x == n {
        return true
    }
    for i:=2; i*i <= x; i++ {
        if math.Pow(float64(i), float64(n)) == float64(x) {
            return true
        }
    }
    return false
}



