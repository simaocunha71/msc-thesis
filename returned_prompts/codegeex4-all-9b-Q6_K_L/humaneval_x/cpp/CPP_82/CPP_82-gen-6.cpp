/*A:*/
// The above code is correct, but it can be optimized by using the following observations:
// If the length of the string is 1 or 2, it is a prime number
// If the length of the string is even, it is not a prime number
// If the length of the string is odd, we can check if it is divisible by any odd number from 3 to the square root of the number
// If we find any odd number that divides it evenly, it is not a prime number
// If we do not find any odd number that divides it evenly, it is a prime number

// Check if the length of the string is a prime number
int length = str.length();
if (length == 1 || length == 2) {
    return true;
}
if (length % 2 ==