Here is a revised version of your code that is more efficient and easier to read:

```c++
#include <iostream>
#include <string>

using namespace std;

bool is_happy(string s) {
    if (s.length() < 3) {
        return false;
    }
    for (int i = 0; i < s.length() - 2; i++) {
        string trio = s.substr(i, 3);
        if (trio.find(trio[0]) != string::npos || trio.find(trio[1]) != string::npos || trio.find(trio[2]) != string::npos) {
            return false;
        }
    }
    return true;
}

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;
    if (is_happy(s)) {
        cout << s << " is happy.\n";
    } else {
        cout << s << " is not happy.\n";
    }
    return 0;
}
```

Explanation of changes:

1. Simplified the condition to check if three consecutive characters are the same. Instead of using three nested loops, we use the `find` method of the `string` class to check if any of the characters in the trio are the same.

2. Removed the unnecessary `using namespace std;` directive from the `main` function. This directive should only be used at the top level of the file.

3. Simplified the output statements. Instead of using `printf`, we use `cout` which is a more modern and C++-standard way of printing output.

4. Removed the unnecessary `c_str()` method call. This method is used to convert a `std::string` object to a