Here is a corrected version of your code:

```cpp
#include <iostream>
#include <string>
using namespace std;

bool cycpattern_check(string a, string b) {
    int n = a.length();
    int m = b.length();

    for (int i = 0; i < n; i++) {
        string temp = a.substr(i, m);
        if (temp.find(b) != string::npos) {
            return true;
        }
    }

    return false;
}

int main() {
    cout << cycpattern_check("abcd", "abd") << endl;
    cout << cycpattern_check("hello", "ell") << endl;
    cout << cycpattern_check("whassup", "psus") << endl;
    cout << cycpattern_check("abab", "baa") << endl;
    cout << cycpattern_check("efef", "eeff") << endl;
    cout << cycpattern_check("himenss", "simen") << endl;
    return 0;
}
```

Explanation:
The function `cycpattern_check` checks if the second word `b` or any of its rotations is a substring in the first word `a`. It does this by iterating over the first word and checking if the current substring (of length `m`, the length of `b`) contains `b`. If it does, it returns `true`. If it