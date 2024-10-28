    letter_map := make(map[rune]int)
    letter_list := strings.Split(test, " ")

    for _, letter := range letter_list {
        letter_map[rune(letter[0])] += 1
    }
    return letter_map
}



