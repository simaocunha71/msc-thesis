    var result = make(map[rune]int)
    var test_runes = []rune(test)

    for _, c := range test_runes {
        if _, ok := result[c]; ok {
            result[c] += 1
        }else{
            result[c] = 1
        }
    }
    return result
}



