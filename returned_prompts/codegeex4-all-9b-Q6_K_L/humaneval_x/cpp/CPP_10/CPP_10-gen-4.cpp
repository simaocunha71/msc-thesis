The code you have written is almost correct, but there is a mistake in the `is_palindrome` function. The `rbegin()` and `rend()` functions return iterators to the reverse beginning and end of the string respectively. These iterators do not directly correspond to the characters of the string, but rather to the positions of the characters. Therefore, when you use them to create a new string, the characters are not in the correct order.

To fix this, you should use the `reverse` function from the C++ Standard Library to reverse the string directly. Here is the corrected code:

```cpp
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool is_palindrome(string str) {
    // Test if given string is a palindrome
    string s(str);
    reverse(s.begin(), s.end());
    return s == str;
}

string make_palindrome(string str) {
    /*
    Find the shortest palindrome that begins with a supplied string. 
    Algorithm idea is simple: - Find the longest postfix of supplied string that is a palindrome. 
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome("") 
    "" 
    >>> make_palindrome("cat") 
    "catac" 
    >>> make_palindrome("cata") 
    "catac" 
    */
    if (is_palindrome(str)) {
        return str;
    }
    for (int i = 0; i < str.size(); i++) {
        string postfix = str.substr(i);
        if (is_palindrome(postfix)) {
            string prefix = str.substr(0, i);
            string reverse_prefix(prefix.rbegin(), prefix.rend());
            return str + reverse_prefix;
        }
    }
    return "";
}

int main() {
    cout << make_palindrome("cat") << endl;  // Output: "catac"
    return 0;
}
```

In the `make_palindrome` function, I first check if the given string is already a palindrome. If it is, I return it directly. Otherwise, I iterate over the string and for each position, I extract the postfix and check if it is a palindrome. If it is, I extract the prefix and reverse it to get the suffix. I then return the original string concatenated with the suffix.