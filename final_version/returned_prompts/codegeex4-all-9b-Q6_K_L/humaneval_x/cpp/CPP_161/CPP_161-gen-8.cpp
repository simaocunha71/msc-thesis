#include <iostream>
#include <string>
using namespace std;
string solve(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            if (islower(s[i])) {
                result += toupper(s[i]);
            } else {
                result += tolower(s[i]);
            }
        } else {
            result += s[i];
        }
    }
    if (result.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") != string::npos) {
        return result;
    } else {
        string reverse_result = "";
        for (int i = result.length() - 1; i >= 0; i--) {
            reverse_result += result[i];
        }
        return reverse_result;
    }
}

B:
#include <iostream>
#include <string>
using namespace std;

string solve(string s) {
    string result = "";
    for (char c : s) {
        if (isalpha(c)) {
            if (islower(c)) {
                result += toupper(c);
            } else {
                result += tolower(c);
            }
        } else {
            result += c;
        }
    }
    if (result.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") != string::npos) {
        string reverse_result = "";
        for (int i = result.length() - 1; i >= 0; i--) {
            reverse_result += result[i];
        }
        return reverse_result;
    } else {
        return result;
    }
}

C:
#include <iostream>
#include <string>
using namespace std;

string solve(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            if (islower(s[i])) {
                result += toupper(s[i]);
            } else {
                result += tolower(s[i]);
            }
        } else {
            result += s[i];
        }
    }
    if (result.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") != string::npos) {
        string reverse_result = "";
        for (int i = result.length() - 1; i >= 0; i--) {
            reverse_result += result[i];
        }
        return reverse_result;
    } else {
        return result;
    }
}

D:
#include <iostream>
#include <string>
using namespace std;

string solve(string s) {
    string result = "";
    for (char