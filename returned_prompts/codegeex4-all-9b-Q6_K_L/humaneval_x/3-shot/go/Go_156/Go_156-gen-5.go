    roman_map := map[rune]int{
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }

    roman_list := make([]rune, 0)

    for _, c := range "mcldxv" {
        for number >= roman_map[c] {
            roman_list = append(roman_list, c)
            number -= roman_map[c]
        }
    }

    return strings.ToLower(string(roman_list))
}

