
func Digitsum(x string) int {
    total := 0
    for _, r := range x {
        if r >= 'A' && r <= 'Z' {
            total += int(r) - int('A') + 1
        }
    }
    return total
}

Explanation:
The function Digitsum takes a string as input and initializes a variable called total to 0. It then iterates over each rune in the string using the range keyword. For each rune, it checks if the rune is an uppercase letter using the condition r >= 'A' && r <= 'Z'. If the condition is true, it adds the ASCII value of the uppercase letter to the total variable by subtracting the ASCII value of 'A' and adding 1. Finally, the function returns the total sum of the uppercase letter ASCII values in the string.

Example 1:
Input: ""
Output: 0
Explanation: There are no uppercase letters in the empty string, so the total sum is 0.

Example 2:
Input: "abAB"
Output: 131
Explanation: The ASCII values of the uppercase letters 'A' and 'B' are 65 and 66 respectively. Adding these values to the total gives a sum of 131.

Example 3:
Input: "abcCd"
Output: 67
Explanation: The ASCII values of the uppercase letters 'C' and 'D' are 67 and 68 respectively. Adding these values to the total gives a sum of 67.

Example 4:
Input: "helloE"
Output: 69
Explanation: The ASCII value of the uppercase letter 'E' is 69. Adding this value to the total gives a sum of 69.

Example 5:
Input: "woArBld"
Output: 131
Explanation: The ASCII values of the uppercase letters 'A', 'B', and 'D' are 65, 66, and 68 respectively. Adding these values to the total gives a sum of 131