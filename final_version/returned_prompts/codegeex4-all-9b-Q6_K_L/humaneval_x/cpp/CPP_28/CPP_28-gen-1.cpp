```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string concatenate(vector<string> strings) {
    string result;
    for (auto &str : strings) {
        result += str;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    string result = concatenate(strings);
    cout << result << endl; // Outputs: abc
    return 0;
}
```
