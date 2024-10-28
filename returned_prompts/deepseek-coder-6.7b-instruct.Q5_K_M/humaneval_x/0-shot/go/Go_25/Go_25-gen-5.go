    var factors []int

    // Divide by 2 until n becomes odd
    for n%2 == 0 {
        factors = append(factors, 2)
        n = n / 2
    }

    // n is now odd, so we can skip one element (Note i = i + 2)
    for i := 3; i <= int(math.Sqrt(float6(n))); i += 2 {
        // While i divides n, append i and divide n
        for n%i == 0 {
            factors = append(factors, i)
            n = n / i
        }
    }

    // This condition is to handle the case when n is a prime number greater than 2
    if n > 2 {
        factors = append(factors, n)
    }

    return factors
}

The above function works by first dividing the number by 2 until it cannot be divided anymore. This is because all even numbers are factors of 2. Then it starts dividing the remaining number by odd numbers starting from 3. The loop continues until the square root of the number.

If the remaining number is greater than 2, it means that the number is a prime number and it is appended to the factors list.

The time complexity of this function is O(sqrt(n)) and the space complexity is O(1) because the space used does not grow with the size of the input.

The function returns a list of prime factors of the given number. The factors are listed in ascending order. The factors are listed the number of times corresponding to how many times they appear in the factorization.

For example, if the input is 8, the function returns [2, 2, 2] because 8 = 2*2*2. If the input is 25, the function returns [5, 5] because 25 = 5*5. If the input is 70, the function returns [2, 5, 7] because 70 = 2*5*7.

This function is used in number theory to factorize numbers. It is also used in cryptography to factorize large numbers, which is the basis of many encryption algorithms.

It is important to note that this function assumes that the input number