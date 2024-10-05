    result := make([]int, len(xs)-1)
    for i := range xs[:len(xs)-1] {
        result[i] = xs[i+1] * int(math.Pow(float64(2), float64(i)))
    }
    return result
}



