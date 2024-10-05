    var even, odd []int
    for _, v := range lst1 {
        if v % 2 == 0 {
            even = append(even, v)
        }else{
            odd = append(odd, v)
        }
    }
    if len(odd) == 0 {
        return "YES"
    }
    for _, v := range lst2 {
        if v % 2 == 0 && len(odd) > 0 {
            return "YES"
        }
    }
    return "NO"
}