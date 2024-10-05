    number_map := map[string]string{
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    }

    number_words := strings.Split(numbers, " ")
    sort.Slice(number_words, func(i, j int) bool {
        return number_map[number_words[i]] < number_map[number_words[j]]
    })

    return strings.Join(number_words, " ")
}



