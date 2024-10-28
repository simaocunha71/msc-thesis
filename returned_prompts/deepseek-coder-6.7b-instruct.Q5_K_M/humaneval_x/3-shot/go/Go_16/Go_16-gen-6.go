    count_map := make(map[rune]int)
    for _, c := range strings.ToLower(str) {
        count_map[c]++
    }

    return len(count_map)
}



