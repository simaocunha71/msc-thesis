    for (int i = word.length()-2; i >= 0; i--) {
        if (isvowel(word[i])) {
            if (isconsonant(word[i-1]) && isconsonant(word[i+1])) {
                return word.substr(i, 1);
            }
        }
    }
    return "";
}

bool isvowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isconsonant(char c) {
    c = tolower(c);
    return !isvowel(c);
}
//test
int main() {
    cout << get_closest_vowel("yogurt") << endl; // "u"
    cout << get_closest_vowel("FULL") << endl; // "U"
    cout << get_closest_vowel("quick") << endl; // ""
    cout << get_closest_vowel("ab") << endl; // ""
    return 0;
} 
#endif 
```

C++ solutions for the given problems:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char c : paren_string) {
        if (c == '(') {
            level++;
            current_paren += c;
        } else if (c == ')') {
            level--;
            current_paren += c;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - int(number);
}

string get_closest_vowel(string word) {
    for (int i = word.length() - 2; i >= 0; i