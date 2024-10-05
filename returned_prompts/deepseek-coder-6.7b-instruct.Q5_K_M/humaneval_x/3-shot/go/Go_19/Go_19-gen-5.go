    num_map := map[string]int{
        "zero":  0,
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,
    }

    str_arr := strings.Split(numbers, " ")
    sort.Slice(str_arr, func(i, j int) bool {
        return num_map[str_arr[i]] < num_map[str_arr[j]]
    })
    return strings.Join(str_arr, " ")
}



