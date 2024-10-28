    result := make(map[rune]int, 0)

    for _, c := range test {
        if _, ok := result[c]; ok {
            result[c]++
        }else{
            result[c] = 1
        }
    }

    return result
}

