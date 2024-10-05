    vector<int> factors;
    // Start from 2 and keep dividing n by i until it is no longer divisible
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}

int main() {
    vector<int> factors;
    factors = factorize(70);
    for(int i = 0; i < factors.size(); i++){
        printf("%d ", factors[i]);
    }
    return 0;
}
```

The program works by continuously dividing the input integer `n` by increasing integers starting from 2. When `n` is no longer divisible by the current integer, the program moves to the next integer and continues the process until `n` is reduced to 1. The remainders are the prime factors of the original input integer.

The time complexity of the program is `O(n)` because in the worst case scenario, the program has to divide `n` by all numbers from 2 to `n`. The space complexity is `O(k)` where `k` is the number of prime factors. This is because the program uses a vector to store the prime factors.

This program is an implementation of the prime factorization algorithm, which is a standard method for factoring integers into their prime components.

## Code Explanation

The code begins by declaring a function named `factorize` that takes an integer `n` as an argument and returns a vector of integers. The function begins by declaring an empty vector named `factors`.

The function then enters a for loop that starts at 2 and continues until `n` is greater than 1. Inside the loop, the code checks if `n` is divisible by the current integer `i`. If `n` is divisible by `i`, the code enters a while loop that continues as long as `n` is divisible by `i`. Inside this loop, the code pushes `i` to the `factors` vector, updates `n` to be `n` divided by `i`, and continues the loop.

After the while loop finishes, the code increments