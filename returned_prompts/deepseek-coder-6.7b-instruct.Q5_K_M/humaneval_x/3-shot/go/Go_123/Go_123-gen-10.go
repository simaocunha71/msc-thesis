    var collatzSequence []int
    collatzSequence = append(collatzSequence, n)

    for n != 1 {
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3 * n + 1
        }
        collatzSequence = append(collatzSequence, n)
    }

    var oddNumbers []int
    for _, num := range collatzSequence {
        if num % 2 != 0 {
            oddNumbers = append(oddNumbers, num)
        }
    }

    sort.Ints(oddNumbers)
    return oddNumbers
}



