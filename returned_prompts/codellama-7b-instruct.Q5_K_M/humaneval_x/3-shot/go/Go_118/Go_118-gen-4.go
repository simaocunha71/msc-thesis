    var left_string []byte
    var right_string []byte
    var left_vowel byte
    var right_vowel byte

    for i := 0; i < len(word); i++{
        if word[i] == word[len(word)-1]{
            continue
        }else if word[i] != word[i+1]{
            left_string = append(left_string, word[i])
            right_string = append(right_string, word[len(word)-i-1])
        }
    }

    for i := 0; i < len(left_string); i++{
        if left_string[i] == 'a' || left_string[i] == 'e' || left_string[i] == 'i' || left_string[i] == 'o' || left_string[i] == 'u'{
            left_vowel = left_string[i]
        }
    }

    for i := 0; i < len(right_string); i++{
        if right_string[i] == 'a' || right_string[i] == 'e' || right_string[i] == 'i' || right_string[i] == 'o' || right_string[i] == 'u'{
            right_vowel = right_string[i]
        }
    }
    if left_vowel == 0 && right_vowel == 0{
        return ""
    }else{
        return string(right_vowel)
    }
}



