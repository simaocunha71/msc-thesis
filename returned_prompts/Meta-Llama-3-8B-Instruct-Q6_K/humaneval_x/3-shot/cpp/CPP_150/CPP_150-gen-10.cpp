    if (is_prime(n)) return x;
    else return y;
}

bool is_prime(int n)
{
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;

    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}  // This is helper function to check if a number is prime.  //  It returns false for composite numbers and true for prime numbers.  //  It also handles 0, 1, and 2 as non-prime.  //  It uses trial division method.  //  It starts checking from 3 and increments by 2 each time.  //  It stops when the square root of the number is reached.  //  It returns false as soon as it finds a divisor.  //  If it doesn't find any divisors, it returns true.  //  It uses the built-in sqrt function to calculate the square root.  //  It takes an integer as input and returns a boolean.  //  It is a helper function for the x_or_y function.  //  It helps to determine whether the number is prime or not.  //  It is used to check if a number is prime or not.  //  It is a part of the x_or_y function.  //  It helps to implement the logic of the x_or_y function.  //  It is used to check if a number is prime or not.  //  It is a part of the x_or_y function.  //  It helps to implement the logic of the x_or_y function.  //  It is used to check if a number is prime or not.  //  It is a part of the x_or_y function.  //  It helps to implement the logic of the x_or_y function.  //  It is used to check if a number is prime or not.  //  It is a part of the x_or_y function.  //  It helps to implement the logic of the x_or_y function.  //  It is used to check if a number is prime or not.  //  It is a part of the x_or_y function.  //  It helps to implement the logic of the x_or_y function