```
func Digitsum(x string) int {
    sum := 0
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char - 'A' + 65)
        }
    }
    return sum
}
```
The function Digitsum takes a string x as input and returns the sum of the ASCII codes of the upper case characters in the string.

In the function, we initialize a variable sum to 0. Then, we iterate over each character in the string using a for loop. For each character, we check if it is an upper case character by checking if it is greater than or equal to 'A' and less than or equal to 'Z'. If it is an upper case character, we add its ASCII code to the sum. The ASCII code of an upper case character is calculated by subtracting the ASCII code of 'A' from the character and adding 65.

Finally, we return the sum. This sum is the sum of the ASCII codes of the upper case characters in the string.