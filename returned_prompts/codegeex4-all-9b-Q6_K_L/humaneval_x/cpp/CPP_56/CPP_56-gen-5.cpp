/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing("><<>")
false
*/
#include <iostream>
#include <string>
using namespace std;

bool correct_bracketing(string brackets) {
    int count = 0;
    for (char c : brackets) {
        if (c == '<') {
            count++;
        } else if (c == '>') {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }
    return count == 0;
}

int main() {
    cout << correct_bracketing("<") << endl; // false
    cout << correct_bracketing("<>") << endl; // true
    cout << correct_bracketing("<<><>>") << endl; // true
    cout << correct_bracketing("><<>") << endl; // false
    return 0;
}

C:
/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing("><<>")
false
*/
#include <iostream>
#include <string>
using namespace std;

bool correct_bracketing(string brackets) {
    int count = 0;
    for (char c : brackets) {
        if (c == '<') {
            count++;
        } else if (c == '>') {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }
    return count == 0;
}

int main() {
    cout << correct_bracketing("<") << endl; // false
    cout << correct_bracketing("<>") << endl; // true
    cout << correct_bracketing("<<><>>") << endl; // true
    cout << correct_bracketing("><<>") << endl; // false
    return 0;
}

D:
/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><