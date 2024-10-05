// Solution
var count int
for _, c := range num {
    switch {
    case c == '2' || c == 'B':
        count++
    case c == '3' || c == 'D':
        count++
    case c == '5' || c == '7':
        count++
    }
}
return count
}

S:
// Solution
var count int
var primeHexDigits = map[rune]bool{
    '2': true, 'B': true,
    '3': true, 'D': true,
    '5': true, '7': true,
}
for _, c := range num {
    if primeHexDigits[c] {
        count++
    }
}
return count
}

P:
// Problem
The problem is asking for a function that takes a hexadecimal number as a string and counts the number of hexadecimal digits that are prime numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. In the context of hexadecimal numbers, the prime digits are 2, 3, 5, 7, B (which is 11 in decimal), and D (which is 13 in decimal).

// Expected Output
The expected output for the given examples are:
- For num = "AB", the output should be 1.
- For num = "1077E", the output should be 2.
- For num = "ABED1A33", the output should be 4.
- For num = "123456789ABCDEF0", the output should be 6.
- For num = "2020", the output should be 2.

// Solution
The problem can be solved by iterating over the input string and checking if each character is a prime hexadecimal digit. The prime hexadecimal digits are 2, 3, 5, 7, B, and D. If a character is a prime hexadecimal digit, increment a counter. The function should return the counter at the end. There are two solutions provided, one using a switch statement and the other using a map. Both solutions achieve the same result.