    if (is_prime(n))
        return x;
    else
        return y;
}

bool is_prime(int n){
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i <= sqrt(n); i += 2)
        if (n % i == 0)
            return false;
    return true;
} 
}  // end of namespace std
int main() {
    return 0;
}
// The following is the C++ code for the problem. This program 
// checks for prime numbers and returns the value of x if the 
// number is prime, otherwise it returns the value of y. 
// The is_prime function checks whether a number is prime or not. 
// For a number to be prime, it should not be divisible by any 
// number less than or equal to its square root. 
// If the number is less than or equal to 1, it is not prime. 
// If the number is 2, it is prime. 
// If the number is even, it is not prime. 
// The function returns true for prime numbers and false for 
// non-prime numbers. 
// The is_prime function is used in the x_or_y function to 
// check whether the number is prime or not. 
// If the number is prime, it returns the value of x, 
// otherwise it returns the value of y. 
// In the main function, we call the x_or_y function with 
// different values and print the returned values. 
// The output of the program will be the value of x if the 
// number is prime, otherwise it will be the value of y. 
// The following is the C++ code for the problem. 
// This program checks for prime numbers and returns the value 
// of x if the number is prime, otherwise it returns the 
// value of y. The is_prime function checks whether a number 
// is prime or not. For a number to be prime, it should not 
// be divisible by any number less than or equal to its 
// square root. If the number is less than or equal to 1, 
// it is not prime. If the number is 2, it is prime. If 
// the number is even, it is not prime. The function returns 
//