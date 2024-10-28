    var (
        first_term, second_term int
        prime_number           int
    )

    for i := 0; i < n; i++ {
        first_term, second_term = second_term, first_term+second_term
        if first_term % 2 == 0 {
            first_term += 1
        }

        prime_number = first_term
        for i := 2; i < int(math.Sqrt(float64(prime_number))); i++ {
            if prime_number % i == 0 {
                prime_number += 1
                i = 1
            }
        }
    }
    return prime_number
}
