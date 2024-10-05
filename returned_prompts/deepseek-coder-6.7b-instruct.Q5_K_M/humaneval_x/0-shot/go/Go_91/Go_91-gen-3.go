    count := 0
    re := regexp.MustCompile(`[.?!]`)
    sentences := re.Split(S, -1)

B:
    for _, sentence := range sentences {
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            count++
        }
    }

    return count
}


