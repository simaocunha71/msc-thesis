
To solve this task I'd suggest to follow these steps:

1. Define a function `isPrime` that will receive a number as an integer and will return `true` if the number is prime and `false` otherwise.

2. Define a function `hexToDecimal` that will receive a hexadecimal digit as a string and will return the decimal equivalent as an integer.

3. Define the main function `HexKey` that will receive the string with hexadecimal digits, will iterate over the string, and will count the numbers that are prime.

4. Call the `HexKey` function with the string "123456789ABCDEF0".

Here's how your final code would look like:

```go
func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func hexToDecimal(s string) int {
    switch s {
    case "0":
        return 0
    case "1":
        return 1
    case "2":
        return 2
    case "3":
        return 3
    case "4":
        return 4
    case "5":
        return 5
    case "6":
        return 6
    case "7":
        return 7
    case "8":
        return 8
    case "9":
        return 9
    case "A":
        return 10
    case "B":
        return 11
    case "C":
        return 12
    case "D":
        return 13
    case "E":
        return 14
    case "F":
        return 15
    }
    return 0
}

func HexKey(num string) int {
    count := 0
    for _, c := range num {
        if isPrime(hexToDecimal(string(c))) {
            count++
        }
    }
    return count
}
``