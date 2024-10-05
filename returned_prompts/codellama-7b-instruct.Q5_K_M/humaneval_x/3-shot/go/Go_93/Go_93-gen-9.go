    var result string
    var result_runes []rune
    var lower_case_alphabet string = "abcdefghijklmnopqrstuvwxyz"
    var upper_case_alphabet string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for _, c := range message {
        if strings.Contains(lower_case_alphabet, string(c)) {
            result_runes = append(result_runes, upper_case_alphabet[lower_case_alphabet.Index(string(c)) + 2])
        } else if strings.Contains(upper_case_alphabet, string(c)) {
            result_runes = append(result_runes, lower_case_alphabet[upper_case_alphabet.Index(string(c)) + 2])
        } else {
            result_runes = append(result_runes, c)
        }
    }
    result = string(result_runes)
    return result
}



