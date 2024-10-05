    numbers_list := strings.Split(numbers, " ")
    sort.Strings(numbers_list)
    result := strings.Join(numbers_list, " ")
    return result
}



