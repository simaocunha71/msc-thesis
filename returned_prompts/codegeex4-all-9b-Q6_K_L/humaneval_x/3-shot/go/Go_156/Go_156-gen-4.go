    roman_map := make(map[int]string)
    roman_map[1] = "i"
    roman_map[4] = "iv"
    roman_map[5] = "v"
    roman_map[9] = "ix"
    roman_map[10] = "x"
    roman_map[40] = "xl"
    roman_map[50] = "l"
    roman_map[90] = "xc"
    roman_map[100] = "c"
    roman_map[400] = "cd"
    roman_map[500] = "d"
    roman_map[900] = "cm"
    roman_map[1000] = "m"

    result := ""

    for i:= 1000; i >= 1; i = i/10{
        if number >= i {
            count := number / i
            number %= i
            result += strings.Repeat(roman_map[i], count)
        }
    }
    return result
}

