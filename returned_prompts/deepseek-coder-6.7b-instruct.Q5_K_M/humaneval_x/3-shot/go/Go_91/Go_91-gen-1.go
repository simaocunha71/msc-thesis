    re := regexp.MustCompile(`[.|?|!] `)
    sentences := re.Split(S, -1)
    count := 0

    for _, sentence := range sentences {
        words := strings.Fields(sentence)
        if len(words) > 0 && words[0] == "I" {
            count++
        }
    }

    return count
}



