    var collatz []int
    for n != 1 {
        if n % 2 != 0 {
            collatz = append(collatz, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    collatz = append(collatz, 1)

    sort.Ints(collatz)
    return collatz
}



