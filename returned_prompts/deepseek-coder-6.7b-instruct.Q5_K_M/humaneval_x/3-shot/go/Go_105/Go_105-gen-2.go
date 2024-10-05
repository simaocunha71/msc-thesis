    var numbers = map[int]string{
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    var valid_numbers []int
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            valid_numbers = append(valid_numbers, num)
        }
    }

    sort.Sort(sort.Reverse(sort.IntSlice(valid_numbers)))

    var result []string
    for _, num := range valid_numbers {
        result = append(result, numbers[num])
    }

    return result
}



