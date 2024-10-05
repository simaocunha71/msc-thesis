    count := 0
    for _, v := range lst1 {
        if v % 2 == 0 {
            count++
        }
    }

    if len(lst1) == count {
        return "YES"
    }

    for _, v := range lst2 {
        if v % 2 == 0 {
            if count < len(lst1) {
                count++
            }
        }
    }
    if count == len(lst1) {
        return "YES"
    } else {
        return "NO"
    }
}



