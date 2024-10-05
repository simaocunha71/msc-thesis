    oddLst1, evenLst2 := 0, 0

    for _, num := range lst1 {
        if num%2 != 0 {
            oddLst1++
        }
    }

    for _, num := range lst2 {
        if num%2 == 0 {
            evenLst2++
        }
    }

    if oddLst1 > evenLst2 {
        return "NO"
    }
    return "YES"
}



