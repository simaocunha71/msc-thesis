    if n<2 {
        return y
    }

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}



