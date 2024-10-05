    result := make([]int, 0)

    for i := 2; i < n; i++ {
        for j := 2; j < int(math.Sqrt(float64(i))); j++ {
            if i%j == 0 {
                break
            }
        }
        result = append(result, i)
    }
    return result
}



