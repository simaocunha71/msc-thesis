    number_list := make([]string, 0)

    for _, n := range strings.Fields(numbers) {
        number_list = append(number_list, n)
    }
    sort.Strings(number_list)

    return strings.Join(number_list, " ")
}



