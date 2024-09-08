    vector<int> res;
    while(n > 1){
        if(n % 2 == 0){
            n /= 2;
        }else{
            n = 3*n + 1;
        }
        if(n % 2 != 0){
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    return res;
}
int main()
{
    printf("%d\n", get_odd_collatz(5).size());
    return 0;
}

Solution:
The idea here is to generate the Collatz sequence until we reach 1, and store all the odd numbers in the sequence.

We start from the given number `n`, and then we apply the Collatz sequence rules to generate the next number in the sequence. If the current number is even, we divide it by 2; if it's odd, we multiply it by 3 and add 1.

We keep doing this until we reach 1. During this process, we store all the odd numbers in a vector `res`. After the sequence is generated, we sort the vector and return it.

Here is the C++ code to implement this:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> get_odd_collatz(int n) {
    vector<int> res;
    while (n > 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        if (n % 2 != 0) {
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main() {
    printf("%d\n", get_odd_collatz(5).size());
    return 0;
}
```

In this code, we define a function `get_odd_collatz` that takes an integer `n` as input and returns a vector of integers. Inside this function, we initialize an empty vector `res` to store the odd numbers in the Collatz sequence.

We then enter a while loop that continues until `n` becomes 1. Inside the loop, we apply the Collatz sequence rules to generate the next number in the sequence. If the current number is even, we divide it by 2; if it's odd, we multiply it by 3 and add 1.

We also check if the current number is odd (using the condition