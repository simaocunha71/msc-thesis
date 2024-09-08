    vector<int> res;
    int i = 2;
    while(i * i <= n){
        if(n % i){
            i++;
        }
        else{
            int count = 0;
            while(n % i == 0){
                n /= i;
                count++;
            }
            res.push_back(i);
            if(count > 1) res.push_back(count);
        }
    }
    if(n > 1) res.push_back(n);
    return res;
}
int main() {
    vector<int> res = factorize(70);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

S:
The solution is correct. However, I would like to improve it. 

Here is a slightly improved version:

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> factorize(int n) {
    vector<int> res;
    for (int i = 2; i * i <= n; i++) {
        int count = 0;
        while (n % i == 0) {
            n /= i;
            count++;
        }
        if (count > 0) {
            res.push_back(i);
            if (count > 1) res.push_back(count);
        }
    }
    if (n > 1) res.push_back(n);
    sort(res.begin(), res.end());
    return res;
}

int main() {
    vector<int> res = factorize(70);
    for (int i = 0; i < res.size(); i++)
        cout << res[i] << " ";
    return 0;
}
```

The improvements I made are:

1.  I used a `for` loop instead of `while` to iterate over the prime numbers. This is because we know that the prime factors of a number are less than or equal to the square root of the number.
2.  I used a `while` loop to count the occurrences of each prime factor. This is because we need to know how many times each prime factor appears in the factorization.
3.  I added a `sort` call at the end of the function to sort the prime factors in ascending order. This is because the problem statement asks for the prime factors in the order from smallest to largest.
4.  I used `cout` instead of `printf` in the `main` function. This is because