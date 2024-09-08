#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
            return false;
        }
    }
    return s.length() >= 3;
}

int main() {
    cout << is_happy("a") << endl;
    cout << is_happy("aa") << endl;
    cout << is_happy("abcd") << endl;
    cout << is_happy("aabb") << endl;
    cout << is_happy("adb") << endl;
    cout << is_happy("xyy") << endl;
    return 0;
}
B:
#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
            return false;
        }
    }
    return s.length() >= 3;
}

int main() {
    cout << is_happy("a") << endl;
    cout << is_happy("aa") << endl;
    cout << is_happy("abcd") << endl;
    cout << is_happy("aabb") << endl;
    cout << is_happy("adb") << endl;
    cout << is_happy("xyy") << endl;
    return 0;
}
C:
#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
            return false;
        }
    }
    return s.length() >= 3;
}

int main() {
    cout << is_happy("a") << endl;
    cout << is_happy("aa") << endl;
    cout << is_happy("abcd") << endl;
    cout << is_happy