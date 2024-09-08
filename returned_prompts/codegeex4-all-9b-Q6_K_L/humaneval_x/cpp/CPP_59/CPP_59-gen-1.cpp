```cpp
int largest_prime_factor(int n){
    int i, largest = 0;
    // Loop through all numbers from 2 to n
    for (i = 2; i <= n; i++) {
        // Check if i is a factor of n
        if (n % i == 0) {
            // Check if i is prime
            bool is_prime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            // Update largest if i is prime and greater than current largest
            if (is_prime && i > largest) {
                largest = i;
            }
        }
    }
    return largest;
}
```
B:
```cpp
int largest_prime_factor(int n){
    int largest = 0;
    // Loop through all numbers from 2 to n
    for (int i = 2; i <= n; i++) {
        // Check if i is a factor of n
        if (n % i == 0) {
            // Check if i is prime
            bool is_prime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            // Update largest if i is prime and greater than current largest
            if (is_prime && i > largest) {
                largest = i;
            }
        }
    }
    return largest;
}
```
C:
```cpp
int largest_prime_factor(int n){
    int i, largest = 0;
    // Loop through all numbers from 2 to n
    for (i = 2; i <= n; i++) {
        // Check if i is a factor of n
        if (n % i == 0) {
            // Check if i is prime
            bool is_prime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            // Update largest if i is prime and greater than current largest
            if (is_prime && i > largest) {
                largest = i;
            }
        }
    }
    return largest;
}
```
D:
```cpp
int largest_prime_factor(int n