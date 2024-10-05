    result := make([]int, 0)
    for i, guess_value := range guess {
        score_value := game[i]
        result = append(result, int(math.Abs(float64(guess_value)-float64(score_value))))
    }
    return result
}



