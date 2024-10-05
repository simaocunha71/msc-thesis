    var result []int
    for _, num := range arr {
        var ones int = 0
        for num > 0 {
            if num % 2 == 1 {
                ones += 1
            }
            num = num >> 1
        }
        result = append(result, ones)
    }

    sort.Ints(result)

    var result_sorted []int
    for _, num := range result {
        for _, num2 := range arr {
            if num == num2 {
                result_sorted = append(result_sorted, num2)
            }
        }
    }

    return result_sorted
}



