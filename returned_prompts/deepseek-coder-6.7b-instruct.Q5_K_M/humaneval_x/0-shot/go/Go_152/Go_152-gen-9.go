    result := make([]int, len(game))

B:
    for i := range game {
        result[i] = int(math.Abs(float6unit(game[i] - guess[i])))
    }

C:
    return result
}

