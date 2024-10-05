    len_s := len(s)
    if len_s < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(len_s))); i++ {
        if len_s%i == 0 {
            return false
        }
    }
    return true
}