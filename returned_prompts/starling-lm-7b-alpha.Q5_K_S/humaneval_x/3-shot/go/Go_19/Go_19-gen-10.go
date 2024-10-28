    numbers_map := map[rune]int{'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list := make([]int, 0)
    for _, c := range numbers {
        if _, ok := numbers_map[c]; ok {
            numbers_list = append(numbers_list, numbers_map[c])
        }
    }
    sort.Ints(numbers_list)

    result := make([]rune, 0)
    for _, n := range numbers_list {
        result = append(result, rune(numbers_map[rune(n)]))
    }
    return string(result)
}



