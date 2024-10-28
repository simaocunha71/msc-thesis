    for i := 2; i < int(math.Sqrt(float64(n))); i+=2 {
        if n-i == i || n-i == 2*i || n-i == 3*i || n-i == 4*i{
            return true
        }
    }
    return false
}



