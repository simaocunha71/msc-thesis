#include <iostream>
using namespace std;
bool is_nested(string str) {
    int n = str.size();
    int count = 0;
    for(int i = 0; i < n; i++) {
        if(str[i] == '[') {
            count++;
        } else if(str[i] == ']') {
            count--;
        }
        if(count == 0) {
            return true;
        }
    }
    return false;
}
int main() {
    cout << is_nested("[[]]") << endl; // 1
    cout << is_nested("[]]]]]]][[[[[]") << endl; // 0
    cout << is_nested("[][]") << endl; // 0
    cout << is_nested("[]") << endl; // 0
    cout << is_nested("[[][]]") << endl; // 1
    cout << is_nested("[[]][[") << endl; // 1
    return 0;
}
B:
#include <iostream>
using namespace std;
bool is_nested(string str) {
    int n = str.size();
    int count = 0;
    for(int i = 0; i < n; i++) {
        if(str[i] == '[') {
            count++;
        } else if(str[i] == ']') {
            count--;
        }
        if(count < 0) {
            return true;
        }
    }
    return false;
}
int main() {
    cout << is_nested("[[]]") << endl; // 1
    cout << is_nested("[]]]]]]][[[[[]") << endl; // 1
    cout << is_nested("[][]") << endl; // 0
    cout << is_nested("[]") << endl; // 0
    cout << is_nested("[[][]]") << endl; // 1
    cout << is_nested("[[]][[") << endl; // 1
    return 0;
}
C:
#include <iostream>
using namespace std;
bool is_nested(string str) {
    int n = str.size();
    int count = 0;
    for(int i = 0; i < n; i++) {
        if(str[i] == '[') {
            count++;
        } else if(str[i] == ']') {
            count--;
        }
        if(count < 0) {
            return false;
        }
    }
    return false;
}
int main() {
    cout << is_nested("[[]]") <<