    var product int
    for n != 0 {
        d := n % 10
        if d % 2 != 0 {
            product *= d
        }
        n /= 10
    }
    return product
}

// Test Cases
fmt.Println(Digits(1))  // 1
fmt.Println(Digits(4))  // 0
fmt.Println(Digits(235)) // 15
fmt.Println(Digits(258)) // 0





In this code,

The Digits function takes an integer as input and returns the product of all odd digits in the integer. If all the digits are even, the function returns 0.

The function uses a for loop to iterate through each digit of the input integer. Inside the loop, it uses the modulus operator (%) to get the last digit of the integer. If the last digit is odd (i.e., not divisible by 2), the function multiplies it with the product variable. Then, it uses integer division (/) to remove the last digit from the integer. This process continues until the integer becomes 0.

After the loop, the function returns the final product of the odd digits.

The Test Cases section demonstrates the usage of the Digits function with different input values and prints the expected output.




The time complexity of this function is O(log(n)), where n is the input integer. This is because the function needs to iterate through each digit of the integer, and the number of digits in an integer is proportional to the logarithm of the integer.

The space complexity is O(1) because the function uses a fixed amount of space to store the product variable, regardless of the input size.





To optimize the code, you can consider using the bitwise AND operator (&) instead of the modulus operator (%) to check if a digit is odd. The bitwise AND operation is faster than the modulus operation, especially for larger integers. Here's an example of how you can modify the code to use bitwise AND:

func Digits(n int) int {
    product := 1
    for n != 0 {
        d :=