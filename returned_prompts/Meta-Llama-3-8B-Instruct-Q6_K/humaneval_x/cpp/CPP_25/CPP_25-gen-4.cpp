Here is the code in C++ that uses a vector to store the prime factors of a given integer.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> factorize(int n) {
    vector<int> result;
    for(int i = 2; i * i <= n; i++) {
        while(n % i == 0) {
            result.push_back(i);
            n /= i;
        }
    }
    if(n > 1) {
        result.push_back(n);
    }
    return result;
}

int main() {
    int n = 70;
    vector<int> res = factorize(n);
    for(int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}
```

This code works by iterating from 2 to the square root of the number, and for each number, it checks if it is a factor of the number. If it is, it adds it to the result vector and divides the number by that factor. This process continues until the number is reduced to 1. If the number is greater than 1 after the loop, it means that the number is a prime number and it is added to the result vector.

In the main function, the code calls the factorize function with the number 70, and then prints the result vector. The output will be the prime factors of 70, which are 2, 5, and 7.