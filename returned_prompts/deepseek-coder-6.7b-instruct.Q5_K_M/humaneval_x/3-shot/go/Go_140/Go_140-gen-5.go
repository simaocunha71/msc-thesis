    var newText = ""
    var spaceCount = 0
    for _, c := range text {
        if c == ' ' {
            spaceCount += 1
            if spaceCount == 2 {
                newText += "-"
            }
        } else {
            if spaceCount > 0 {
                newText += "_"
                spaceCount = 0
            }
            newText += string(c)
        }
    }
    return newText
}



