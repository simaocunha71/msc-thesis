
    // Return false for 0 and 1
    if n <= 1 {
        return false
    }

    // Return true for 2, 3, 5, 7, 11, ...
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}
