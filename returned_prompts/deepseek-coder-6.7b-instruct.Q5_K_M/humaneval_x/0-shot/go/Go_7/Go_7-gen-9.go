    var filteredList []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }
    return filteredList
}

func main() {
    fmt.Println(FilterBySubstring([]string{}, "a"))
    fmt.Println(FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, "a"))
}

