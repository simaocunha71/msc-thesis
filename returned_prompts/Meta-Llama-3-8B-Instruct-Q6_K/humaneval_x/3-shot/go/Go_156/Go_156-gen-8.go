    roman := make(map[int]string)
    roman[1000] = "m"
    roman[900] = "cm"
    roman[500] = "d"
    roman[400] = "cd"
    roman[100] = "c"
    roman[90] = "xc"
    roman[50] = "l"
    roman[40] = "xl"
    roman[10] = "x"
    roman[9] = "ix"
    roman[5] = "v"
    roman[4] = "iv"
    roman[1] = "i"

    result := ""
    for key, value := range roman {
        for number >= key {
            result += value
            number -= key
        }
    }
    return strings.ToLower(result)
}