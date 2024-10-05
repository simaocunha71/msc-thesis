func UniqueDigits(x []int) []int {
    result := make([]int, 0)
    for _, num := range x {
        hasEven := false
        for _, digit := range strconv.Itoa(num) {
            if (digit-'0')%2 == 0 {
                hasEven = true
                break
            }
        }
        if !hasEven {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}