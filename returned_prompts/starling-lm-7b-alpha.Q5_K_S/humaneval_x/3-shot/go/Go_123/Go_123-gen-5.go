    result := make([]int, 0)

    var current_number int = n
    for current_number != 1 {
        if current_number % 2 == 0 {
            current_number /= 2
        }else {
            current_number = 3 * current_number + 1
            result = append(result, current_number)
        }
    }
    sort.Ints(result)
    return result
}



