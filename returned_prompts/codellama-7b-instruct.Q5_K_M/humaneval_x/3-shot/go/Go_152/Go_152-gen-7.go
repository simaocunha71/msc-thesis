    result := make([]int, len(game))
    for i, v := range game{
        if v == guess[i]{
            result[i] = 0
        }else{
            result[i] = math.Abs(guess[i]-v)
        }
    }
    return result
}



