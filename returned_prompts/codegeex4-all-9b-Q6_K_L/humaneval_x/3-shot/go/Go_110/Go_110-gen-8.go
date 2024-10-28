    var count1 int = 0
    var count2 int = 0

    for _, number := range lst1 {
        if number % 2 == 1 {
            count1 += 1
        }
    }

    for _, number := range lst2 {
        if number % 2 == 0 {
            count2 += 1
        }
    }

    if count1 <= count2 {
        return "YES"
    }

    return "NO"
}

