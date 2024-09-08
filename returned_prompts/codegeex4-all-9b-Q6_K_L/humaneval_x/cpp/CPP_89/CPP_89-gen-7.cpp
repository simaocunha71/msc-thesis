#include <iostream>
#include <string>
using namespace std;
string encrypt(string s) {
    string res = "";
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            c = (c - 'a' + 4) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            c = (c - 'A' + 4) % 26 + 'A';
        }
        res += c;
    }
    return res;
}

// Driver code
int main() {
    string s = "hi";
    cout << encrypt(s) << endl;  // Output: lm
    s = "asdfghjkl";
    cout << encrypt(s) << endl;  // Output: ewhjklnop
    s = "gf";
    cout << encrypt(s) << endl;  // Output: kj
    s = "et";
    cout << encrypt(s) << endl;  // Output: ix
    return 0;
}