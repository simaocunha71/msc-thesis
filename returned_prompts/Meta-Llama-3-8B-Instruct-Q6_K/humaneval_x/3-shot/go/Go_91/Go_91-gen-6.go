    var boredoms int
    s = regexp.MustCompile(`\s+`).ReplaceAllString(S, " ")
    sentences := strings.Split(s, "[.!?]")
    for _, sentence := range sentences {
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            boredoms++
        }
    }
    return boredoms
}