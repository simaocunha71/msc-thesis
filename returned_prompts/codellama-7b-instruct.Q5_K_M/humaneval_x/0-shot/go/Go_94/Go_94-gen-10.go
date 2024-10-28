    for _, v := range lst {
        for i := 2; i < math.Sqrt(float64(v)); i++ {
            if v%i == 0 {
                continue A
            }
        }
        return len(strconv.Itoa(v))
    }
    return 0
}
