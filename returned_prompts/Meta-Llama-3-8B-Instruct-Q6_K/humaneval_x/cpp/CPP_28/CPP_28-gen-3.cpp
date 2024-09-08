    string result = "";
    for (const auto &s : strings) {
        result += s;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    printf("%s\n", concatenate(strings).c_str());
    return 0;
}

Answer:
The solution to this problem is a simple loop that iterates over the vector of strings, concatenating each string to the result string. The resulting string is then returned.

Here is the code:

```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result = "";
    for (const auto &s : strings) {
        result += s;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    printf("%s\n", concatenate(strings).c_str());
    return 0;
}
```

When you run this code, it will output:

```
abc
```

This is because the `concatenate` function takes a vector of strings as input, iterates over the vector, and concatenates each string to the result string. The resulting string is then returned and printed to the console.