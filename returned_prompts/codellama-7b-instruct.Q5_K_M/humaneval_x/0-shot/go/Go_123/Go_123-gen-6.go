    if n == 1 {
        return []int{1}
    }
    var collatz []int
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            continue
        }
        collatz = append(collatz, i)
        for i != 1 {
            if i%2 == 0 {
                i = i / 2
            } else {
                i = 3*i + 1
            }
            collatz = append(collatz, i)
        }
    }
    sort.Ints(collatz)
    return collatz
}
