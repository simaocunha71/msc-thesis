func Exchange(lst1, lst2 []int) string {
    even1, odd1 := 0, 0
    even2, odd2 := 0, 0
    for _, v := range lst1 {
        if v%2 == 0 {
            even1++
        } else {
            odd1++
        }
    }
    for _, v := range lst2 {
        if v%2 == 0 {
            even2++
        } else {
            odd2++
        }
    }
    if odd1 > even2 {
        return "NO"
    }
    return "YES"
}