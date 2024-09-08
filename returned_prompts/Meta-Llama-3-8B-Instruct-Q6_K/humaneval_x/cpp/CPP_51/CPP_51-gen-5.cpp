    string s = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] != 'a' && text[i] != 'e' && text[i] != 'i' && text[i] != 'o' && text[i] != 'u' && text[i] != 'A' && text[i] != 'E' && text[i] != 'I' && text[i] != 'O' && text[i] != 'U'){
            s = s + text[i];
        }
    }
    return s;
}

int main(){
    string text = "abcdef\nghijklm";
    printf("%s\n", remove_vowels(text).c_str());
    return 0;
}

B:
#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string remove_vowels(string text) {
    string result;
    for (char c : text) {
        if (!isalpha(c) || (c >= 'a' && c <= 'z' && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') ||
            (c >= 'A' && c <= 'Z' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U')) {
            result += c;
        }
    }
    return result;
}

int main() {
    string text = "abcdef\nghijklm";
    cout << remove_vowels(text) << endl;
    return 0;
}

C:
#include <iostream>
#include <string>

using namespace std;

string remove_vowels(string text) {
    string result;
    for (char c : text) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            continue;
        }
        result += c;
    }
    return result;
}

int main() {
    string text = "abcdef\nghijklm";
    cout << remove_vowels(text) << endl;
    return 0;
}

D:
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string remove_vowels(string text) {
