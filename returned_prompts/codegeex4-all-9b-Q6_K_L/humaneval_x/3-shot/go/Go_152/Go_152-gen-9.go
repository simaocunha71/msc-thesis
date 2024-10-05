    result := make([]int, 0)
    for i := 0; i < len(guess); i++ {
        result = append(result, int(math.Abs(float64(guess[i]-game[i]))))
    }
    return result
}