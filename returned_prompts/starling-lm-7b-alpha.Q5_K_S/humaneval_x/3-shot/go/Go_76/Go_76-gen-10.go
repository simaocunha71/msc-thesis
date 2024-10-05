    for i := 0; i <= 31; i++ {
        if int(math.Pow(float64(n), float64(i))) == x {
            return true
        }
    }
    return false
}



