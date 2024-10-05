    int largest = 2;
    while (n % 2 == 0){
        n = n / 2;
    }
    for (int i = 3; i * i <= n; i = i + 2){
        while (n % i == 0){
            largest = i;
            n = n / i;
        }
    }
    if (n > 2){
        largest = n;
    }
    return largest;
}

int main(){
    printf("%d\n", largest_prime_factor(13195));
    printf("%d\n", largest_prime_factor(2048));
    return 0;
}

*/


int main() {
    cout << largest_prime_factor(13195) << endl;
    cout << largest_prime_factor(2048) << endl;
    return 0;
}
```

## Testing

```
g++ -std=c++11 main.cpp -o main
./main
```

## Output

```
29
2
```

## Explanation

This program works by continuously dividing the input number by the smallest possible prime number (starting from 2) until the number is no longer divisible. The largest prime number that was found in this process is the largest prime factor of the input number. 

For example, for the number 13195, it first checks if it is divisible by 2. It is, so it divides it by 2 and the remainder is 13195/2 = 6597. It then checks if 6597 is divisible by 3, which it is. It divides it by 3 and the remainder is 6597/3 = 2199. It then checks if 2199 is divisible by 5, which it is. It divides it by 5 and the remainder is 2199/5 = 439.8. It then checks if 439.8 is divisible by 7, which it is. It divides it by 7 and the remainder is 439.8/7 = 61. It then checks if