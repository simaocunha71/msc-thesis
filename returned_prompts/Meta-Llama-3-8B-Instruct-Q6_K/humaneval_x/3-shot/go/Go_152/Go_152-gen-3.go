    result := make([]int, 0)
    for i := 0; i < len(game); i++ {
        if game[i] == guess[i] {
            result = append(result, 0)
        } else {
            result = append(result, int(math.Abs(float64(guess[i] - game[i]))))
        }
    }
    return result
}