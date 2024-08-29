#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

string get_closest_vowel(string word){

    for (int i = word.length() - 3; i >= 0; i--) {

        if (isalpha(word[i]) && isalpha(word[i+1]) && isalpha(word[i+2])) {

            if (is_consonant(word[i]) && is_consonant(word[i+2])) {

                if (is_vowel(word[i+1])) {

                    return string(1, word[i+1]);
                }
            }
        }
    }

    return "";
}

bool is_consonant(char c) {
    c = tolower(c);
    return !is_vowel(c) && isalpha(c);
}

bool is_vowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    string word;
    cin >> word;
    cout << get_closest_vowel(word) << endl;
    return 0;
}
B:
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

string get_closest_vowel(string word){

    for (int i = word.length() - 3; i >= 0; i--) {

        if (isalpha(word[i]) && isalpha(word[i+1]) && isalpha(word[i+2])) {

            if (is_consonant(word[i]) && is_consonant(word[i+2])) {

                if (is_vowel(word[i+1])) {

                    return string(1, word[i+1]);
                }
            }
        }
    }

    return "";
}

bool is_consonant(char c) {
    c = tolower(c);
    return !is_vowel(c) && isalpha(c);
}

bool is_vowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    string word;
    cin >> word;
    cout << get_closest_vowel(word) << endl;
    return 0;
}
C:
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

string get_closest_vowel(string word){

    for (int i = word.length