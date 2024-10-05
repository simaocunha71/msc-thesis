    vector<int> factors;
    for(int i = 2; i*i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n /= i;
        }
    }
    if(n != 1)
        factors.push_back(n);
    return factors;
}
int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    vector<int> primes = factorize(num);
    printf("Prime factors: ");
    for(int i = 0; i < primes.size(); i++) {
        printf("%d ", primes[i]);
    }
    return 0;
}
```

This program factors a given number into its prime factors and stores them in a vector. It then prints these factors to the console. The program uses the method of continually dividing the number by its smallest factor until the number is no longer divisible, then moving on to the next smallest factor. If the remaining number is greater than 1, it is a prime factor and is added to the vector.

The complexity of this program is O(sqrt(n)) because in the worst case, it divides the number by all numbers up to its square root.

Please note that this program does not handle negative numbers or zero. If you need to handle these cases, you should add error checking to the factorize function.

```python
def factorize(n):
    factors = []
    i = 2
    while i*i <= n:
        while n % i:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

num = int(input("Enter a number: "))
primes = factorize(num)
print("Prime factors:", primes)
```

This Python version of the program does the same thing as the C++ version. It reads a number from the user, factors it into prime factors, and prints these factors.

This Python version also uses list appending instead of vector pushing back for the same reason as the C++ version.

The complexity of this program is