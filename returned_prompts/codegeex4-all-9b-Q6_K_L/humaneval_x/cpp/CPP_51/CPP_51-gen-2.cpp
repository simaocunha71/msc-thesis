#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string remove_vowels(string text) {
    string vowels = "aeiouAEIOU";
    for (char& c : text) {
        if (vowels.find(c) != string::npos) {
            c = ' ';
        }
    }
    text.erase(remove(text.begin(), text.end(), ' '), text.end());
    return text;
}

int main() {
    string str;
    getline(cin, str);
    cout << remove_vowels(str) << endl;
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

string remove_vowels(string text) {
    string vowels = "aeiouAEIOU";
    string result;
    for (char c : text) {
        if (vowels.find(c) == string::npos) {
            result += c;
        }
    }
    return result;
}

int main() {
    string str;
    getline(cin, str);
    cout << remove_vowels(str) << endl;
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

string remove_vowels(string text) {
    string result;
    for (char c : text) {
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' &&
            c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
            result += c;
        }
    }
    return result;
}

int main() {
    string str;
    getline(cin, str);
    cout << remove_vowels(str) << endl;
    return 0;
}

D:
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string remove_vowels(string text) {
    string vowels = "aeiouAEIOU";
    string result = text;
    for (char& c : result) {
        if (vowels.find(c) != string::npos) {
            c = ' ';
        }
    }
    result.erase(remove(result.begin(), result.end(), ' '), result.end());
    return result;
}

int main() {
    string str;
    getline(cin, str);
    cout << remove_vowels(str) << endl;
    return 0;
}

在这几个选项中