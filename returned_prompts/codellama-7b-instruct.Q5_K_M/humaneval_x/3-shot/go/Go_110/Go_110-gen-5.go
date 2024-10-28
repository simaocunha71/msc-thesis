    for _, element := range lst1 {
        if element%2 != 0 {
            return "NO"
        }
    }

    for _, element := range lst2 {
        if element%2 == 0 {
            return "YES"
        }
    }

    return "NO"
}



