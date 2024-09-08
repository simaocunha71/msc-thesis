```cpp
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "db";
    while (decimal > 0) {
        binary += (decimal % 2 == 0) ? "0" : "1";
        decimal /= 2;
    }
    reverse(binary.begin(), binary.end());
    binary += "db";
    return binary;
}
```