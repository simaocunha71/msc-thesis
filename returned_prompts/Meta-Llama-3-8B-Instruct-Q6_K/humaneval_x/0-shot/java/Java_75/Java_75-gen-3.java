        // Check if the number is divisible by 2
        if (a % 2 == 0) {
            a /= 2;
        }

        // Check if the number is divisible by 3
        if (a % 3 == 0) {
            a /= 3;
        }

        // Check if the number is divisible by 5
        if (a % 5 == 0) {
            a /= 5;
        }

        // If the number is not divisible by 2, 3 or 5, then it is prime
        if (a > 1) {
            return true;
        }

        // If the number is less than 1, then it is not a product of 3 prime numbers
        return false;
    }
}
// It is not a good solution as it doesn't check if the remaining number is prime.
// It also doesn't check for the remaining two prime numbers.
// The remaining two prime numbers can be checked by using a loop.
// The loop should start from the next prime number and end at the square root of the remaining number.
// The loop should check if the remaining number is divisible by the current number.
// If it is divisible, then the remaining number is divided by the current number and the loop continues.
// If it is not divisible, then the current number is checked if it is prime.
// If it is prime, then the remaining number is divided by the current number and the loop continues.
// If the remaining number becomes 1, then the function returns true.
// If the remaining number becomes less than 1, then the function returns false.
// The function should also check if the remaining number is less than 2.
// If it is, then the function should return false.
// The function should also check if the remaining number is greater than 1.
// If it is, then the function should return true.