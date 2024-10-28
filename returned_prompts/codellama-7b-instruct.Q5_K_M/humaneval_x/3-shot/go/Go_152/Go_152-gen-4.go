    result := make([]int, len(game))

    for i, v := range game {
        result[i] = abs(v-guess[i])
    }
    return result
}



