    var prime_numbers = [26]int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    var result string

    for _, word := range strings.Split(sentence, " ") {
        if contains(prime_numbers, len(word)) {
            result += word + " "
        }
    }

    return strings.TrimRight(result, " ")
}

func contains(slice []int, item int) bool {
    set := make(map[int]struct{}, len(slice))
    for _, elem := range slice {
        set[elem] = struct{}{}
    }
    _, ok := set[item]
    return ok
}



