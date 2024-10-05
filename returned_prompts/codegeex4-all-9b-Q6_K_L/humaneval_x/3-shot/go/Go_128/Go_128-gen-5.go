    if len(arr) == 0 {
        return nil
    } else {
        var sum float64 = 0
        var product int = 1

        for _, v := range arr {
            sum += math.Abs(float64(v))
            product *= int(math.Pow(-1, float64(v)))
        }
        return sum * float64(product)
    }
}



