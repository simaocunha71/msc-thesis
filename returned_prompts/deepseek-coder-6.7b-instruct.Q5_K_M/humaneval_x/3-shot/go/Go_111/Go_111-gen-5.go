    count := make(map[rune]int)
    for _, c := range test {
        count[c]++
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



