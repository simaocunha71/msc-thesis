    var even1, odd1, even2, odd2 int

    for _, num := range lst1 {
        if num%2 == 0 {
            even1++
        } else {
            odd1++
        }
    }

    for _, num := range lst2 {
        if num%2 == 0 {
            even2++
        } else {
            odd2++
        }
    }

    if odd1 <= even2 {
        return "YES"
    }

    return "NO"
}