    var max_word string = ""
    var max_count int = 0

    for _, word := range words{
        count := 0
        for _, c := range word{
            if !strings.ContainsRune(max_word, c){
                count += 1
            }
        }
        if count > max_count{
            max_word = word
            max_count = count
        }else if count == max_count{
            if word < max_word{
                max_word = word
            }
        }
    }

    return max_word
}

