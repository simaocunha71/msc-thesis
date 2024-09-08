    string result = "";
    while(x > 0){
        int r = x % base;
        if(r < 10)
            result = to_string(r) + result;
        else if(r == 10)
            result = "A" + result;
        else if(r == 11)
            result = "B" + result;
        else if(r == 12)
            result = "C" + result;
        else if(r == 13)
            result = "D" + result;
        else if(r == 14)
            result = "E" + result;
        else if(r == 15)
            result = "F" + result;
        x /= base;
    }
    return result;
}

int main()
{
    int x = 8;
    int base = 3;
    cout<<change_base(x,base)<<endl;
    return 0;
}

B:
```c
#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int r = x % base;
        if (r < 10)
            result = to_string(r) + result;
        else if (r < 16)
            result = (char) ('A' + r - 10) + result;
        x /= base;
    }
    return result;
}

int main() {
    int x = 8;
    int base = 3;
    cout << change_base(x, base) << endl;
    return 0;
}
```

Explanation:
The function `change_base` takes two integer parameters, `x` and `base`, and returns a string representation of `x` in the given base.

The function works by repeatedly dividing `x` by `base` and appending the remainder to the result string. If the remainder is less than 10, it is converted to a string using `to_string`. If the remainder is 10 or greater, it is converted to a character using the ASCII value of the character ('A' to 'F' for 10 to 15) and appended to the result string.

In the `main` function, we call `change_base` with `x = 8` and `base = 3`, and print the result to the console.

The time complexity of this function is O(log(x)), where x is the input number, because we divide `x` by `base`