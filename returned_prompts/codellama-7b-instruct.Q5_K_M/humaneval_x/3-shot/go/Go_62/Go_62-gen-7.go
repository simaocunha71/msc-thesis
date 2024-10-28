    result := make([]int, len(xs)-1)
    for i, x := range xs[:len(xs)-1] {
        result[i] = x * int(math.Pow(2, float64(i)))
    }
    return result
}



