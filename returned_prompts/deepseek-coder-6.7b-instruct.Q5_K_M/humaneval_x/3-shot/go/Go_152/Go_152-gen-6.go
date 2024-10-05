    diff  := make([]int, len(game))
    for i:= range game {
        diff[i] = int(math.Abs(float64(game[i]-guess[i])))
    }
    return diff
}



