    int max = 2;
    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            if(i > max){
                max = i;
            }
            while(n % i == 0){
                n /= i;
            }
        }
    }
    return max;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Largest prime factor of %d is: %d\n", n, largest_prime_factor(n));
    return 0;
}

Explanation:
This program calculates the largest prime factor of a given number. It does this by iterating from 2 to the given number, and for each number, it checks if it is a factor of the given number. If it is a factor, it checks if it is a prime number (i.e., it has no factors other than 1 and itself). If it is a prime number, it updates the maximum prime factor and then divides the given number by the prime factor. This process continues until the given number is reduced to 1. Finally, the program returns the maximum prime factor.

The `largest_prime_factor` function takes an integer `n` as input and returns the largest prime factor of `n`. The function iterates from 2 to `n`, and for each number `i`, it checks if `i` is a factor of `n` using the modulo operator (`%`). If `i` is a factor, it checks if `i` is a prime number by checking if `i` has any factors other than 1 and itself. If `i` is a prime number, it updates the maximum prime factor and then divides `n` by `i` using integer division (`/`). This process continues until `n` is reduced to 1. Finally, the function returns the maximum prime factor.

In the `main` function, the program prompts the user to enter a number, calls the `largest_prime_factor` function with the entered number, and prints the result. The program uses the `scanf` function to read the input number and the `printf` function to print the result.

Note that the program assumes that the input number is greater than 1 and is not a prime number. If the input number is 1 or a prime number, the program will not return the correct result. Also, the program uses a simple iterative approach to find the largest prime factor, which