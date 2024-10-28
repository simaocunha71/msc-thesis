    var result string = ""
    for _, c := range message {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'{
            result += string(strings.ToUpper(string(c)))
        }else if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            result += string(strings.ToLower(string(c)))
        }else if c >= 'a' && c < 'e'{
            result += string(c + 2)
        }else if c >= 'E' && c < 'i'{
            result += string(c - 2)
        }else if c >= 'i' && c < 'o'{
            result += string(c + 2)
        }else if c >= 'O' && c < 'u'{
            result += string(c - 2)
        }else if c >= 'u' && c < 'A'{
            result += string(c + 2)
        }else if c >= 'a' && c < 'A'{
            result += string(c - 2)
        }else{
            result += string(c)
        }
    }
    return result
}



