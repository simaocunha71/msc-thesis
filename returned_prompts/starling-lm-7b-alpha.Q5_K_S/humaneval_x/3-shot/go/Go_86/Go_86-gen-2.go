    words := strings.Split(s, " ")
    result := make([]string, 0)
    for _, word := range words {
        var char_list []rune
        for _, c := range word {
            char_list = append(char_list, c)
        }
        sort.Slice(char_list, func(i, j int) bool {
            return int(char_list[i]) < int(char_list[j])
        })
        result = append(result, string(char_list))
    }
    return strings.Join(result, " ")
}



