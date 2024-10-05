    words := strings.Fields(test)
    histogram := make(map[rune]int)

    for _, word := range words {
        for _, char := range word {
            histogram[char] += 1
        }
    }

    max := 0
    for _, value := range histogram {
        if value > max {
            max = value
        }
    }

    result := make(map[rune]int)
    for key, value := range histogram {
        if value == max {
            result[key] = value
        }
    }

    return result
}



