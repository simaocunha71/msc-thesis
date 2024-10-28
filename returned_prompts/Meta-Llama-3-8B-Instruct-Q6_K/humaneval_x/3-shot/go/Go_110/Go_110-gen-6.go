    evenCount := 0
    for _, num := range lst1 {
        if num%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    for _, num := range lst2 {
        if num%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    return "NO"
}