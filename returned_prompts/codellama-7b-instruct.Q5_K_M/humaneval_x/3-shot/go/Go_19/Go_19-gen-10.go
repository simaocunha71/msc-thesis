    var number_list = strings.Fields(numbers)
    var sorted_list = make([]string, 0)

    for _, number := range number_list{
        switch number{
        case "zero":
            sorted_list = append(sorted_list, "zero")
        case "one":
            sorted_list = append(sorted_list, "one")
        case "two":
            sorted_list = append(sorted_list, "two")
        case "three":
            sorted_list = append(sorted_list, "three")
        case "four":
            sorted_list = append(sorted_list, "four")
        case "five":
            sorted_list = append(sorted_list, "five")
        case "six":
            sorted_list = append(sorted_list, "six")
        case "seven":
            sorted_list = append(sorted_list, "seven")
        case "eight":
            sorted_list = append(sorted_list, "eight")
        case "nine":
            sorted_list = append(sorted_list, "nine")
        }
    }
    sort.Strings(sorted_list)
    return strings.Join(sorted_list, " ")
}




