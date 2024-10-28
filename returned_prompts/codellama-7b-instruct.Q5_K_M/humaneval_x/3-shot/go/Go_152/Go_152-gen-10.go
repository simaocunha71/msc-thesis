    result := make([]int, len(guess))
    for i, v := range game {
        if v == guess[i]{
            result[i] = 0
        }else{
            result[i] = abs(v-guess[i])
        }
    }
    return result
}



