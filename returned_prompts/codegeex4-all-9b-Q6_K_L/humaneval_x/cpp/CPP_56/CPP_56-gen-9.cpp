#include <stack>
#include <iostream>
#include <string>
using namespace std;

bool correct_bracketing(string brackets) {
    stack<char> s;
    for (int i = 0; i < brackets.length(); i++) {
        if (brackets[i] == '<') {
            s.push(brackets[i]);
        } else if (brackets[i] == '>') {
            if (s.empty()) {
                return false;
            }
            s.pop();
        }
    }
    if (s.empty()) {
        return true;
    } else {
        return false;
    }
}

int main() {
    cout << correct_bracketing("<") << endl; // false
    cout << correct_bracketing("<>") << endl; // true
    cout << correct_bracketing("<<><>>") << endl; // true
    cout << correct_bracketing("><<>") << endl; // false
    return 0;
}