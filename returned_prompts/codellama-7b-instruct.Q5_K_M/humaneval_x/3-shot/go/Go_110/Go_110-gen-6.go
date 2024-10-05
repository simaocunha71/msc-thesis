    var (
        all_even bool
        even_count int
    )

    for _, num := range lst1 {
        if num % 2 == 0 {
            even_count++
        }
    }

    if even_count == len(lst1) {
        all_even = true
    }

    for _, num := range lst2 {
        if num % 2 != 0 {
            all_even = false
            break
        }
    }

    if all_even {
        return "YES"
    }

    return "NO"
}



