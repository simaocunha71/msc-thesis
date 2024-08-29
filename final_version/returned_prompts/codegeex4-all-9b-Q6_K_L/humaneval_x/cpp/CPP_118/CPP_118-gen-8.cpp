#include <iostream>
#include <string>
using namespace std;

string get_closest_vowel(string word) {
    string vowels = "aeiouAEIOU";
    int n = word.length();
    for (int i = n - 1; i >= 0; --i) {
        if (vowels.find(word[i]) != string::npos && i != 0 && i != n - 1) {
            if (vowels.find(word[i - 1]) == string::npos && vowels.find(word[i + 1]) == string::npos) {
                return word[i];
            }
        }
    }
    return "";
}

int main() {
    cout << get_closest_vowel("yogurt") << endl;  // Output: u
    cout << get_closest_vowel("FULL") << endl;    // Output: U
    cout << get_closest_vowel("quick") << endl;  // Output: 
    cout << get_closest_vowel("ab") << endl;     // Output: 
    return 0;
}

