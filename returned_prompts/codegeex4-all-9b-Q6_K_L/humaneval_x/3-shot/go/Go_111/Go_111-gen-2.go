    result := make(map[rune]int)
    for _, c := range test {
        if _, ok := result[c]; ok {
            result[c] += 1
        }else{
            result[c] = 1
        }
    }
    return result
}

