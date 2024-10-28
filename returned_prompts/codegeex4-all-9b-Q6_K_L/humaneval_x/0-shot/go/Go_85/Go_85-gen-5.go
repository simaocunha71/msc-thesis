func Add(lst []int) int {
    result := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i]%2 == 0 {
            result += lst[i]
        }
    }
    return result
}
