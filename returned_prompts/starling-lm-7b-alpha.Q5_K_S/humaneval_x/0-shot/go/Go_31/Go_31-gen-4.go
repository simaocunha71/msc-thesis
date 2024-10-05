
func IsPrime(n int) bool {
    if n == 1 || n == 0 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

The IsPrime function checks if a given number n is prime or not. It first checks if the number is equal to 1 or 0. If it is, the function immediately returns false, as 1 and 0 are not prime numbers.

Next, the function starts a loop from 2 to the square root of n (i*i <= n). It checks if n is divisible by any number in this range. If it is, the function immediately returns false, as it means n has a factor other than 1 and itself, and therefore is not prime.

If the loop completes without finding any factors, the function returns true, indicating that the number is prime.

To use the function, you can call it with a number as an argument. For example, to check if 6 is prime, you can write:

fmt.Println(IsPrime(6))

This will output false, as 6 is not a prime number. Similarly, you can check other numbers by replacing 6 with the desired number in the function call.

Here are some additional examples of using the IsPrime function:

fmt.Println(IsPrime(101)) // true
fmt.Println(IsPrime(11)) // true
fmt.Println(IsPrime(13441)) // true
fmt.Println(IsPrime(61)) // true
fmt.Println(IsPrime(4)) // false
fmt.Println(IsPrime(1)) // false

Each of these function calls will return the result of whether the given number is prime or not, allowing you to verify the correctness of the function implementation.

In summary, the IsPrime function is a useful tool for determining if a given number is prime or not. It follows a simple and efficient algorithm to quickly determine the result, and can be easily integrated into any program that requires prime number checking functionality.

By following the steps outlined in the solution, you can create a