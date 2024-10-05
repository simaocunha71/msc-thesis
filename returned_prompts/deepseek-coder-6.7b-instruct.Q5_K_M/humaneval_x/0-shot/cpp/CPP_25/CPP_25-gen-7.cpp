    vector<int> factors;
    // Divide n by 2 until n is odd
    while (n % 2 == 0){
        factors.push_back(2);
        n = n / 2;
    }
    // n must be odd at this point, thus skip the even numbers and iterate only for odd.
    for (int i = 3; i * i <= n; i = i + 2){
        // while i divides n, append i and divide n
        while (n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    // this condition is to handle the case when n is a prime number greater than 2
    if (n > 2)
        factors.push_back(n);
    return factors;
}

int main() {
    vector<int> factors = factorize(8);
    for(int i = 0; i < factors.size(); i++)
        printf("%d ", factors[i]);
    return 0;
}
```

## Testing

```c++
int main() {
    vector<int> factors = factorize(8);
    for(int i = 0; i < factors.size(); i++)
        printf("%d ", factors[i]);
    return 0;
}
```

## Output

```
2 2 2
```

## Explanation

The code works by continuously dividing the input number by 2 until it is odd. Then, it starts to divide the number by odd numbers starting from 3, until it is no longer possible. If the remaining number is greater than 2, it is considered a prime number and is added to the factors. The factors are returned in a vector in ascending order.

## Time complexity

The time complexity of the code is O(sqrt(n)), where n is the input number. This is because in the worst case scenario, the code iterates over the numbers up to the square root of n. The space complexity is O(log n) in the case of large numbers as the code stores the prime factors in a vector.

## Space complexity

The space complexity of the code is O(log n), where n is the