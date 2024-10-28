
#include <iostream>
#include <string>
using namespace std;

bool is_nested(string str) {
    int open_count = 0;
    int close_count = 0;
    for (char c : str) {
        if (c == '[') {
            open_count++;
        } else if (c == ']') {
            close_count++;
        }
        if (close_count > open_count) {
            return true;
        }
    }
    return false;
}

int main() {
    string str = "[[]]";
    cout << is_nested(str) << endl;
    return 0;
}






































































































































































































