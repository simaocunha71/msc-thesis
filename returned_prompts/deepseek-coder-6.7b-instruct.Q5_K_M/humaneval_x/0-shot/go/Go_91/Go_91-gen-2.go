    count := 0
    words := strings.Fields(S)

B:
    for _, word := range words {
        if word[0:1] == "I" {
            count++
        }
    }

    return count
}

I've replaced the regular expression with a simple strings.Fields function. This function splits the input string S on whitespace and returns a slice of words. Then it iterates through this slice, checking if the first letter of each word is "I". If so, it increments count. The function then returns count.

