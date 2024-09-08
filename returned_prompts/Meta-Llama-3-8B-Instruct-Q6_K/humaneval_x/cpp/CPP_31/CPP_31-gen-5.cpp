    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6)); //false
    printf("%d\n", is_prime(101)); //true
    printf("%d\n", is_prime(11)); //true
    printf("%d\n", is_prime(13441)); //true
    printf("%d\n", is_prime(61)); //true
    printf("%d\n", is_prime(4)); //false
    printf("%d\n", is_prime(1)); //false
    return 0;
}

B:
The function is_prime checks if a given number is prime or not. It takes a long long integer as an argument. The function first checks if the number is less than or equal to 1, in which case it is not prime. Then it starts checking from 2 and goes up to the square root of the number. If the number is divisible by any of these values, it is not prime. If it is not divisible by any of these values, it is prime.

In the main function, we test the function with different inputs. The function returns a boolean value, which is printed out using printf. The boolean values are converted to integers using the %d format specifier in printf. The function works correctly for all the test cases. The function is_prime is a correct solution for this problem.

C:
The code provided is a correct solution to the problem. It defines a function is_prime that takes an integer as input and returns true if the number is prime, and false otherwise. The function uses a for loop to check if the number has any divisors other than 1 and itself. If it finds a divisor, it returns false. If it doesn't find any divisors, it returns true.

The main function tests the is_prime function with different inputs and prints the results. The results are correct for all the test cases. The code is well-structured and easy to understand.

D:
The code provided is a correct solution to the problem. It defines a function is_prime that takes an integer as input and returns true if the number is prime, and false otherwise. The function uses a for loop to check if the number has any divisors other than 1 and itself. If it finds a divisor, it