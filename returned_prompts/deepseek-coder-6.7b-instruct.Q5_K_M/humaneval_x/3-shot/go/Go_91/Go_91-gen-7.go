    re := regexp.MustCompile(`[.?!]`)
    sentences := re.Split(S, -1)
    count := 0

    for _, sentence := range sentences {
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            count++
        }
    }
    return count
}



