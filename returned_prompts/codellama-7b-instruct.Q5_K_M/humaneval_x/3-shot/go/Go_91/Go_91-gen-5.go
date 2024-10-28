    var boredom_counter int = 0
    var sentence_regexp = regexp.MustCompile(`^[Ii]`)

    for _, sentence := range strings.Split(S, ".[?!]") {
        if sentence_regexp.MatchString(sentence) {
            boredom_counter += 1
        }
    }
    return boredom_counter
}



