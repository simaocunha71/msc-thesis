    result := make(map[rune]int, 0)

    for _, c := range test {
        result[c] += 1
    }

    return result
}



