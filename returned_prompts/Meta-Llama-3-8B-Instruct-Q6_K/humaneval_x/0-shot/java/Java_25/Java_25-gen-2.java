        List<Integer> result = new ArrayList<>();
        int i = 2;
        while (i * i <= n) {
            while (n % i == 0) {
                result.add(i);
                n /= i;
            }
            i++;
        }
        if (n > 1) {
            result.add(n);
        }
        return result;
    }
}

Explanation:
The function `factorize(int n)` takes an integer `n` as input and returns a list of its prime factors. The prime factors are listed in the order from smallest to largest, and each factor is listed the number of times it appears in the factorization of `n`. 

The algorithm used is a simple trial division approach, where we start from the smallest prime number (2) and keep dividing `n` by the current prime number as long as it is divisible. The prime number is added to the result list each time it is divided from `n`. 

We continue this process until `i * i` is greater than `n`. If `n` is greater than 1 at the end of the loop, it means that `n` is a prime number itself, so we add it to the result list. 

Finally, we return the list of prime factors. 

The time complexity of this algorithm is O(sqrt(n)), where `n` is the input number. This is because we are dividing `n` by each prime number up to its square root. The space complexity is O(n), where `n` is the number of prime factors of the input number. This is because we are storing each prime factor in the result list. 

For example, if the input number is 8, the function will return `[2, 2, 2]`, because 8 is equal to `2^3`. If the input number is 25, the function will return `[5, 5]`, because 25 is equal to `5^2`. If the input number is 70, the function will return `[2, 5, 7]`, because 70 is equal to `2 * 5 * 7`. 

The unit tests provided in the problem statement demonstrate the expected behavior of the function. 

The function can be called with different input numbers to get their prime factorizations. For example, `factorize(8)` returns `[2, 2, 2]`, `factorize(25)` returns `[5, 5]`, and `factorize(