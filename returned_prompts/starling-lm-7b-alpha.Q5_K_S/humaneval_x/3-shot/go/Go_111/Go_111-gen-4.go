    result := make(map[rune]int)

    for _, char := range test {
        if _, ok := result[char]; ok {
            result[char] += 1
        }else {
            result[char] = 1
        }
    }

    return result
}



