    count1 := 0
    count2 := 0
    for _, num := range lst1 {
        if num%2 == 0 {
            count1++
        }
    }

    for _, num := range lst2 {
        if num%2 == 0 {
            count2++
        }
    }

    if count1 == 0 && count2 == 0 {
        return "NO"
    } else if count1 == 0 {
        return "YES"
    } else if count2 == 0 {
        return "NO"
    } else {
        return "YES"
    }
}

