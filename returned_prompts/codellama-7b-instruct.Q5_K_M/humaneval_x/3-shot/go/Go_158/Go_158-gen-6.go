    // find max length string
    var max_length int = 0
    var max_string string = ""
    for _, word := range words{
        if len(word) > max_length{
            max_length = len(word)
            max_string = word
        }
    }

    // sort letters in max string
    letters := make([]rune, 0)
    for _, letter := range max_string{
        letters = append(letters, letter)
    }
    sort.Slice(letters, func(i,j int)bool{
        return letters[i] < letters[j]
    })

    // check if sorted letters are unique
    for i:=0; i<len(letters)-1;i++{
        if letters[i] == letters[i+1]{
            max_string = ""
            break
        }
    }
    return max_string
}



