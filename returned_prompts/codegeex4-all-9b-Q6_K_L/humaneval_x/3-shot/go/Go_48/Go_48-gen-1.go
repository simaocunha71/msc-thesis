    var reversed_text string = ""
    for i := len(text)-1; i >=0; i--{
        reversed_text += string(text[i])
    }
    return text == reversed_text
}



