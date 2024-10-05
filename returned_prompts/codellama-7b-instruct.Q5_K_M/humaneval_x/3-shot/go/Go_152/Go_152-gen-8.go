    result := make([]int, 0)

    for i := 0; i < len(game); i++{
        if game[i] == guess[i]{
            result = append(result, 0)
        }else{
            result = append(result, math.Abs(int(game[i]-guess[i])))
        }
    }
    return result
}



