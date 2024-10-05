    filteredString := []rune{}
    for _,c2 := range s {
        if !strings.Contains(c,string(c2)) {
            filteredString = append(filteredString,c2)
        }
    }
    filteredStringStr := string(filteredString)
    return [2]interface{}{filteredStringStr,strings.EqualFold(filteredStringStr,strings.Reverse(filteredStringStr))}
}