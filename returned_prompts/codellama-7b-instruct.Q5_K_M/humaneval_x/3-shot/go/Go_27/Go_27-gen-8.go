    var result string = ""
    for _, c := range str{
        if strings.Contains("abcdefghijklmnopqrstuvwxyz", string(c)){
            result += strings.ToUpper(string(c))
        }else if strings.Contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ", string(c)){
            result += strings.ToLower(string(c))
        }else{
            result += string(c)
        }
    }
    return result
}



