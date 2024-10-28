    var result strings.Builder
    message_runes := []rune(message)
    for _, c := range message_runes{
        if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'){
            if c >= 'a' && c <= 'z'{
                if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'{
                    result.WriteRune(c + 2)
                }else{
                    result.WriteRune(c)
                }
            }else{
                if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'{
                    result.WriteRune(c + 2)
                }else{
                    result.WriteRune(c)
                }
            }
        }else{
            result.WriteRune(c)
        }
    }
    return result.String()
}



