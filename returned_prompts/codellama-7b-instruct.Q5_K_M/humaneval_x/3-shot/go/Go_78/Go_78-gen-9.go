    var count int = 0
    var hex_digits = map[string]int{
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    for _, c := range num {
        if _, ok := hex_digits[string(c)]; ok {
            count += 1
        }
    }

    return count
}



