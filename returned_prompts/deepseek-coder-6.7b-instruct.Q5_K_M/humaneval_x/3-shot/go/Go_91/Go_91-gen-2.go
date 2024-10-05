    re := regexp.MustCompile(`(?i)^I`)
    sentences := regexp.MustCompile(`[.|?|!]`)
    split_sentences := sentences.Split(S, -1)
    count := 0

    for _, sentence := range split_sentences {
        if re.MatchString(strings.TrimSpace(sentence)) {
            count += 1
        }
    }
    return count
}



