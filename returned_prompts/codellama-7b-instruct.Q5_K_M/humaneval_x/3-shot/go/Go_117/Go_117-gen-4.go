    result := make([]string, 0)

    var words []string = strings.Fields(s)
    for _, word := range words{
        var vowels []rune = []rune{'a','e','i','o','u'}
        var consonants []rune = []rune{'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

        var cnt_vowels int = 0
        var cnt_consonants int = 0
        var cnt_chars int = 0

        for _, c := range word{
            if (bytes.Contains(vowels,[]byte{c})) {
                cnt_vowels += 1
            } else if (bytes.Contains(consonants,[]byte{c})) {
                cnt_consonants += 1
            }
            cnt_chars += 1
        }

        if (cnt_vowels == n){
            result = append(result, word)
        }
    }

    return result
}



