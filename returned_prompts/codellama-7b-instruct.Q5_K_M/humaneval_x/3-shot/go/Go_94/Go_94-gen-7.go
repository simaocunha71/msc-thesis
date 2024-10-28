    var largest_prime int = 0
    var sum int = 0
    for i := 0; i < len(lst); i++ {
        if lst[i] > largest_prime {
            largest_prime = lst[i]
        }
    }

    if largest_prime == 0 {
        return 0
    }

    for i := 0; i < len(strconv.Itoa(largest_prime)); i++ {
        sum += int(strconv.Itoa(largest_prime)[i]-'0')
    }

    return sum
}



