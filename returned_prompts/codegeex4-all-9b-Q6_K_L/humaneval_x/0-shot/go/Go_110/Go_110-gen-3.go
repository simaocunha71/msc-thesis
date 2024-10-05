func Exchange(lst1, lst2 []int) string {
    even := 0
    odd := 0
    for _, num := range lst1 {
        if num % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    for _, num := range lst2 {
        if num % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    if even >= odd {
        return "YES"
    }
    return "NO"
}