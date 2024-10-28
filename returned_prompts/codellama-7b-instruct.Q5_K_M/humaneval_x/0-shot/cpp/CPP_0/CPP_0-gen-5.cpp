/*
Write a function, which takes a string as input, and returns true if the string
is a palindrome, and false otherwise.
*/
#include <iostream>
#include <string>

using namespace std;

bool is_palindrome(string s) {
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    cout << is_palindrome("racecar") << endl;
    cout << is_palindrome("civic") << endl;
    cout << is_palindrome("hello") << endl;
    cout << is_palindrome("level") << endl;
    cout << is_palindrome("rotator") << endl;
    return 0;
}

