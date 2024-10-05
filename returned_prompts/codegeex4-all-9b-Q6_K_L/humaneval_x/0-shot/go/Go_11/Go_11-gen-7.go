func StringXor(a string, b string) string {
    if a == b {
        return "0"
    }

    // convert strings to runes
    arunes := []rune(a)
    brunes := []rune(b)

    // get the length of the longer string
    length := len(arunes)
    if len(brunes) > length {
        length = len(brunes)
    }

    // create a new string to store the result
    result := make([]rune, length)

    // iterate over the runes and perform XOR
    for i := 0; i < length; i++ {
        if i < len(arunes) && i < len(brunes) {
            result[i] = arunes[i] ^ brunes[i]
        } else if i < len(arunes) {
            result[i] = arunes[i]
        } else {
            result[i] = brunes[i]
        }
    }

    return string(result)
}