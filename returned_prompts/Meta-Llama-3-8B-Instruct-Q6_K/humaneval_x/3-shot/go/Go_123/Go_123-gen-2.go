    result := make([]int, 0)
    temp := n
    for temp != 1 {
        if temp % 2 == 0 {
            temp = temp / 2
        } else {
            temp = 3 * temp + 1
        }
        if temp % 2 != 0 {
            result = append(result, temp)
        }
    }
    sort.Ints(result)
    return result
}