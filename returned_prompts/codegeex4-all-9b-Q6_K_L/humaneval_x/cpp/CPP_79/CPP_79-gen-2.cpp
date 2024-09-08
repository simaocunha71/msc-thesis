```cpp
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "";
    while (decimal > 0) {
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}
```

This solution works by repeatedly dividing the decimal number by 2 and prepending the remainder to the binary string. The loop continues until the decimal number is reduced to 0. Finally, the "db" characters are added to the beginning and end of the binary string.