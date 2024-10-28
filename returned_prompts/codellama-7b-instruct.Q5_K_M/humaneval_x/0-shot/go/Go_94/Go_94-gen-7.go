    for _, v := range lst {
        for i := 2; i <= int(math.Sqrt(float64(v))); i++ {
            if v%i == 0 {
                continue A
            }
        }
        return strconv.Atoi(strconv.Itoa(v))
    }
    return 0
}
