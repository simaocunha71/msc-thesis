        if(n <= 1)
            return false;

        for(int i = 2; i <= Math.sqrt(n); i++) {
            if(n % i == 0)
                return false;
        }
        return true;
    }
}
Solution solution = new Solution();
System.out.println(solution.isPrime(6)); // false
System.out.println(solution.isPrime(101)); // true
System.out.println(solution.isPrime(11)); // true
System.out.println(solution.isPrime(13441)); // true
System.out.println(solution.isPrime(61)); // true
System.out.println(solution.isPrime(4)); // false
System.out.println(solution.isPrime(1)); // false

Output:
false
true
true
true
true
false
false
C++ version of this code would look something like this:
```c
#include <iostream>
#include <cmath>

bool isPrime(int n) {
    if(n <= 1)
        return false;

    for(int i = 2; i <= std::sqrt(n); i++) {
        if(n % i == 0)
            return false;
    }
    return true;
}

int main() {
    Solution solution;
    std::cout << solution.isPrime(6) << std::endl; // false
    std::cout << solution.isPrime(101) << std::endl; // true
    std::cout << solution.isPrime(11) << std::endl; // true
    std::cout << solution.isPrime(13441) << std::endl; // true
    std::cout << solution.isPrime(61) << std::endl; // true
    std::cout << solution.isPrime(4) << std::endl; // false
    std::cout << solution.isPrime(1) << std::endl; // false
    return 0;
}
```



This code defines a method `isPrime` that takes an integer `n` as input and returns `true` if `n` is a prime number, and `false` otherwise. The method uses a simple trial division algorithm to check for primality. It iterates from 2 to the square root of `n` and checks if `n` is divisible by any of these numbers. If it is, then `n` is not a prime number and the method returns `false`. If `n` is not divisible by any of these numbers, then it is a prime number and the method returns `true`.

