    int i = 0;
    while(pow(n, i) <= x){
        if(pow(n, i) == x)
            return true;
        i++;
    }
    return false;
}

int main(){
    printf("%d\n", is_simple_power(1, 4)); // true
    printf("%d\n", is_simple_power(2, 2)); // true
    printf("%d\n", is_simple_power(8, 2)); // true
    printf("%d\n", is_simple_power(3, 2)); // false
    printf("%d\n", is_simple_power(3, 1)); // false
    printf("%d\n", is_simple_power(5, 3)); // false
    return 0;
}


A: This is a simple task, but there is a much easier way to do it.
You can use logarithmic properties to simplify the problem.

Here is the code:

```cpp
#include<bits/stdc++.h>
using namespace std;

bool is_simple_power(int x, int n)
{
    if (x < 1) return false;
    double res = log(x) / log(n);
    return res == (int)res;
}

int main()
{
    cout << is_simple_power(1, 4) << endl; // true
    cout << is_simple_power(2, 2) << endl; // true
    cout << is_simple_power(8, 2) << endl; // true
    cout << is_simple_power(3, 2) << endl; // false
    cout << is_simple_power(3, 1) << endl; // false
    cout << is_simple_power(5, 3) << endl; // false
    return 0;
}
```

This program works by using the property of logarithms that log(a^b) = b * log(a). It then checks if the result is an integer, indicating that x is a simple power of n.

It's important to note that this solution works only for positive numbers