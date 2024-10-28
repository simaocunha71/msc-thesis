    var number_list []string
    number_list = strings.Split(numbers, " ")
    sort.Strings(number_list)
    return strings.Join(number_list, " ")
}



