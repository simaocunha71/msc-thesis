    int x = cbrt(a);
    return a == x * x * x;
}
int main() {
    printf("%d\n", iscuber(1));
    printf("%d\n", iscuber(2));
    printf("%d\n", iscuber(-1));
    printf("%d\n", iscuber(64));
    printf("%d\n", iscuber(0));
    printf("%d\n", iscuber(180));

    return 0;
}


A: There is no need to use C++ here. The function iscuber() can be written in C++ as well. Here is the C++ solution:

```cpp
#include <iostream>
#include <cmath>

bool iscuber(int a) {
    int x = cbrt(a);
    return a == x * x * x;
}

int main() {
    std::cout << std::boolalpha << iscuber(1) << std::endl;
    std::cout << std::boolalpha << iscuber(2) << std::endl;
    std::cout << std::boolalpha << iscuber(-1) << std::endl;
    std::cout << std::boolalpha << iscuber(64) << std::endl;
    std::cout << std::boolalpha << iscuber(0) << std::endl;
    std::cout << std::boolalpha << iscuber(180) << std::endl;

    return 0;
}
```

This program will output:

```
true
false
true
true
true
false
```

The cbrt() function calculates the cube root of a number. If the cube of this root is equal to the original number, then it is a cube number.

The std::boolalpha is used to print boolean values as true or false, instead of 1 or 0.

I hope this helps. Let me know if you have any further questions.


A: This is a simple task that can be done with Python. Here is the Python solution:

```