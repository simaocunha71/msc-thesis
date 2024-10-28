    numbers := make([]int, 0)
    names := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    result := make([]string, 0)

    for _, num := range arr {
        if num >= 1 && num <= 9 {
            numbers = append(numbers, num)
        }
    }

    sort.Ints(numbers)
    for i := len(numbers) - 1; i >= 0; i-- {
        result = append(result, names[numbers[i]-1])
    }

    return result
}



