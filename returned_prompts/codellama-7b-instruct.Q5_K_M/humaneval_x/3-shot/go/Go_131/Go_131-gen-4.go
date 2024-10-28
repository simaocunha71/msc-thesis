    result := 0
    string_of_n := strconv.Itoa(n)

    for _, c := range string_of_n {
        if string(c) == "1" || string(c) == "3" || string(c) == "5" || string(c) == "7" || string(c) == "9" {
            result += int(string(c)[0]-'0')
        }
    }
    return result
}



