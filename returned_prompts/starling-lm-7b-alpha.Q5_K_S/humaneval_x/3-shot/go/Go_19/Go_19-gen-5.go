    numbers_slice := strings.Fields(numbers)
    sort.Strings(numbers_slice)
    return strings.Join(numbers_slice, " ")
}



