    count := make(map[rune]int)

    for _, char := range strings.ToLower(test) {
        count[char]++
    }

    max := 0
    for _, v := range count {
        if v > max {
            max = v
        }
    }

    result := make(map[rune]int)
    for k, v := range count {
        if v == max {
            result[k] = v
        }
    }

    return result
}



