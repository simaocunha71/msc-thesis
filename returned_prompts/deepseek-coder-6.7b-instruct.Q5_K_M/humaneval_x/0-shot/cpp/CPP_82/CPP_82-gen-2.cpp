    int n = str.length();
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    printf("%d\n", prime_length("Hello"));
    printf("%d\n", prime_length("abcdcba"));
    printf("%d\n", prime_length("kittens"));
    printf("%d\n", prime_length("orange"));
    return 0;
}

*/

#include<iostream>
#include<string>
using namespace std;

bool prime_length(string str){
    int len = str.length();
    if (len <= 1)
        return false;
    for (int i = 2; i * i <= len; i++) {
        if (len % i == 0)
            return false;
    }
    return true;
}

int main() {
    cout << prime_length("Hello") << endl;
    cout << prime_length("abcdcba") << endl;
    cout << prime_length("kittens") << endl;
    cout << prime_length("orange") << endl;
    return 0;
}
```

## Output
```
1
1
1
0
```

The output shows true (1) for the strings that have a prime number length and false (0) for those that don't.

## Explanation
The function `prime_length(string str)` checks if the length of the input string is a prime number. It first checks if the length is less than or equal to 1, in which case it returns false since prime numbers are defined as being greater than 1. Then it checks if the length is divisible by any number up to the square root of the length. If it is divisible, then it returns false, otherwise it returns true. The square root of the length is used because a larger factor of the number would be a multiple of smaller factor that has already been checked.

In the main function, we call this function with the given inputs and print the results.
