    histogram := make(map[rune]int)
    for _, c := range test {
        histogram[c]++
    }
    return histogram
}



