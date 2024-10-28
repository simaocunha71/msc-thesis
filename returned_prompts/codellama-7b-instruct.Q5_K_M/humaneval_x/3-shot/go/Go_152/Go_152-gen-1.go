    result := make([]int, len(game))
    for i := 0; i < len(game); i++ {
        if game[i] == guess[i]{
            result[i] = 0
        }else {
            result[i] = math.Abs(game[i] - guess[i])
        }
    }
    return result
}



