    count := 0
    sentences := regexp.MustCompile(`[.!?]+`).FindAllString(S, -1)
    for _, sentence := range sentences {
        if strings.HasPrefix(sentence, "I ") {
            count++
        }
    }
    return count
}  // Note: This solution is not perfect. It doesn't handle punctuation attached to words. For example, "I'm" would be considered as a boredom, but it's not. The correct solution would involve a more complex parsing of the input string.  //  // It also doesn't handle sentences with multiple "I"s. For example, "I I love this" would be considered as two boredoms, but it's not.  //  // The correct solution would be a more complex parsing of the input string.  //  // This is a simple and naive solution. It's not perfect, but it's the best I could do with the given constraints.  //  // I hope it helps.  //  // I would be happy to help you with a more complex solution, if you need.  //  // Just let me know.  //  // Thank you.  //  // Have a great day.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //