    odd1, odd2 := 0, 0

    for _, num := range lst1 {
        if num % 2 != 0 {
            odd1++
        }
    }

    for _, num := range lst2 {
        if num % 2 != 0 {
            odd2++
        }
    }

    if odd1 > odd2 {
        return "NO"
    } else {
        return "YES"
    }
}



