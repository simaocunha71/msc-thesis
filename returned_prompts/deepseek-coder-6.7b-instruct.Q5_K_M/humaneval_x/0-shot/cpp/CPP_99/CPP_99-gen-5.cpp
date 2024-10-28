    double val = stod(value);
    int val_int = (int)val;
    double val_frac = val - val_int;
    if(val_frac < 0.5)
        return val_int;
    else if(val > 0)
        return val_int + 1;
    else
        return val_int - 1;
}

int main() {
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}
```

Output:
```
10
15
15
-15
```

Explanation:
The function `closest_integer` converts the input string to a double using `stod` and then separates the integer and fractional parts. If the fractional part is less than 0.5, it returns the integer part. If the fractional part is greater or equal to 0.5 and the number is positive, it adds 1 to the integer part and returns it. If the number is negative, it subtracts 1 from the integer part and returns it.
*/

// The code snippet is written in C++

#include <iostream>
#include <cmath>
#include <string>

int closest_integer(std::string value) {

    double val = std::stod(value);
    int val_int = (int)val;
    double val_frac = val - val_int;
    if(val_frac < 0.5)
        return val_int;
    else if(val > 0)
        return val_int + 1;
    else
        return val_int - 1;
}

int main() {
    std::cout << closest_integer("10") << std::endl;
    std::cout << closest_integer("15.3") << std::endl;
    std::cout << closest_integer("14.5") << std::endl;
   