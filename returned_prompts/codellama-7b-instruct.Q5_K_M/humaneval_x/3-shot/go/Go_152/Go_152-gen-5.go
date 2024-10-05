    result := make([]int, len(game))
    for i, _ := range game {
        if game[i] == guess[i] {
            result[i] = 0
        }else{
            result[i] = abs(guess[i] - game[i])
        }
    }
    return result
}



