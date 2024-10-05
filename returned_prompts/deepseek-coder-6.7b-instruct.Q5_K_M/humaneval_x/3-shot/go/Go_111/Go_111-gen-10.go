    count := make(map[rune]int)
    for _, letter := range strings.Fields(test) {
        for _, char := range letter {
            count[char]++
        }
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



