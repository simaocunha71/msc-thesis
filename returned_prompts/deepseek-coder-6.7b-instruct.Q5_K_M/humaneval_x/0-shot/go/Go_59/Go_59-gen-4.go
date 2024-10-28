
    // Check divisibility by 2
    if n % 2 == 0 {
        return 2
    }

B:

    // Check divisibility by 3
    if n % 3 == 0 {
        return 3
    }

C:

    // Check divisibility by 5
    if n % 5 == 0 {
        return 5
    }

D:

    // Check divisibility by 7
    if n % 7 == 0 {
        return 7
    }

E:

    // Check divisibility by 11
    if n % 11 == 0 {
        return 11
    }

F:

    // Check divisibility by 13
    if n % 13 == 0 {
        return 13
    }

G:

    // Check divisibility by 17
    if n % 17 == 0 {
        return 17
    }

H:

    // Check divisibility by 19
    if n % 19 == 0 {
        return 19
    }

I:

    // Check divisibility by 23
    if n % 23 == 0 {
        return 23
    }

J:

    // Check divisibility by 29
    if n % 29 == 0 {
        return 29
    }

K:

    // Check divisibility by 31
    if n % 31 == 0 {
        return 31
    }

L:

    // If no other prime factors exist, return the number itself
    return n
}

func main() {
    fmt.Println(LargestPrimeFactor(13195))  // 29
    fmt.Println(LargestPrimeFactor(2048))   // 2
}
```

This program checks for the largest prime factor of a number by dividing it by successive numbers, starting from 2. The numbers it checks for are the first 15 prime numbers.

The function `Larg