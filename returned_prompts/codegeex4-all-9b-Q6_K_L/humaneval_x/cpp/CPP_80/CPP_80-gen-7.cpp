/*
You are given a string s.
Your task is to check if the string is happy or not.
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
For example:
is_happy("a") => false
is_happy("aa") => false
is_happy("abcd") => true
is_happy("aabb") => false
is_happy("adb") => true
is_happy("xyy") => false
*/

#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    if (s.length() < 3) {
        return false;
    }
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
            return false;
        }
    }
    return true;
}

int main() {
    string input;
    cout << "Enter a string: ";
    cin >> input;
    if (is_happy(input)) {
        cout << "The string is happy." << endl;
    } else {
        cout << "The string is not happy." << endl;
    }
    return 0;
}
请问上述代码有什么错误

上述代码在检查字符串是否快乐时存在一个逻辑错误。在判断字符串是否快乐时，我们应该检查每三个连续的字符是否不同，而不是检查每个字符是否与前两个字符不同。因此，在循环中，我们应该检查 `s[i]`、`s[i+1]` 和 `s[i+2]` 是否都不同，而不是检查 `s[i]`、`s[i+1]` 和 `s[i+2]` 是否都等于 `s[i]`。

以下是修正后的代码：

```cpp
#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    if (s.length() < 3) {
        return false;
    }
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
            return false;
        }
    }
    return true;
}

int