    re := regexp.MustCompile(`(?i)^I`)
    sentences := regexp.MustCompile(`[.|?|!]`)
    count := 0

    for _, sentence := range sentences.Split(S, -1) {
        if re.MatchString(strings.TrimSpace(sentence)) {
            count++
        }
    }
    return count
}



