    letter_count := make(map[rune]int)
    letters := strings.Split(test, " ")
    for _, letter := range letters{
        if _, ok := letter_count[rune(letter[0])]; ok{
            letter_count[rune(letter[0])] += 1
        }else{
            letter_count[rune(letter[0])] = 1
        }
    }
    return letter_count
}



