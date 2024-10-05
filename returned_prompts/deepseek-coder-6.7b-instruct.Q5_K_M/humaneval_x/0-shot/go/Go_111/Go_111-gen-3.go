    words := strings.Fields(test)
    histogram := make(map[rune]int)

    for _, word := range words {
        for _, letter := range word {
            histogram[letter]++
        }
    }

    max := 0
    for _, v := range histogram {
        if v > max {
            max = v
        }
    }

    result := make(map[rune]int)
    for k, v := range histogram {
        if v == max {
            result[k] = v
        }
    }

    return result
}

