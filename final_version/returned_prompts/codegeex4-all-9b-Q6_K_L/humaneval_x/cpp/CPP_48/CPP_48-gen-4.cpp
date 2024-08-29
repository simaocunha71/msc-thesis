#include <iostream>
using namespace std;

bool is_palindrome(string text) {
    int n = text.size();
    for (int i = 0; i < n / 2; i++) {
        if (text[i] != text[n - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main() {
    cout << is_palindrome("") << endl;  // true
    cout << is_palindrome("aba") << endl;  // true
    cout << is_palindrome("aaaaa") << endl;  // true
    cout << is_palindrome("zbcd") << endl;  // false
    return 0;
}