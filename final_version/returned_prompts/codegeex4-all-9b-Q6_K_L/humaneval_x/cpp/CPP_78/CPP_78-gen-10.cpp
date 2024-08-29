To solve the problem of counting the number of prime hexadecimal digits in a given string, we can follow these steps:

1. Create a string `s` containing the prime hexadecimal digits: `"237BD"`.
2. Initialize a counter `c` to zero.
3. Iterate over each character in the input string `num`.
4. For each character, check if it exists in the string `s` using the `find` method of the `string` class.
5. If the character is found in `s`, increment the counter `c` by one.
6. After the loop, return the value of `c` as the result.

Here is the modified code:

```cpp
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;

int hex_key(string num) {
    int c = 0;
    int n = num.length();
    string s = "237BD";
    for(int i = 0; i < n; i++) {
        if(s.find(num[i]) != string::npos) {
            c++;
        }
    }
    return c;
}

int main() {
    string s = "ABED1A33";
    printf("%d\n", hex_key(s));
    return 0;
}
```

In this code, the `hex_key` function takes a string `num` as input and returns the count of prime hexadecimal digits in `num`. The `main` function demonstrates the usage of the `hex_key` function with the example string `"ABED1A33"`.