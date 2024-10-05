    for i := 0; i < len(game); i++ {
        if game[i] == guess[i] {
            continue A
        } else {
            return []int{abs(game[i] - guess[i])}
        }
    }
    return []int{0}
}
