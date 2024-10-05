    var largestPrime int
    var sumOfDigits int

    // Find largest prime number in the list
    for _, num := range lst {
        if IsPrime(num) && num > largestPrime {
            largestPrime = num
        }
    }

    // Convert the prime number to a string, then iterate through each digit
    // and add it to sumOf