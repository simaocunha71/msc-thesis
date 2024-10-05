    result := make([]int, 0)
    num := n
    for num != 1 {
        if num % 2 != 0 {
            result = append(result, num)
        }
        if num % 2 == 0 {
            num = num / 2
        } else {
            num = num * 3 + 1
        }
    }
    sort.Ints(result)
    return result
}