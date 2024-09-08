    string closest_vowel ="";
    for(int i = word.size()-1; i > 0; i--){
        if(isvowel(word[i])){
            if(closest_vowel == ""){
                closest_vowel = word[i];
            }
            else{
                return closest_vowel;
            }
        }
    }
    return closest_vowel;
}
bool isvowel(char ch){
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}
int main(){
    printf("%s\n", get_closest_vowel("yogurt").c_str());
    printf("%s\n", get_closest_vowel("FULL").c_str());
    printf("%s\n", get_closest_vowel("quick").c_str());
    printf("%s\n", get_closest_vowel("ab").c_str());
    return 0;
}
B:
```c
#include <iostream>
#include <string>
using namespace std;

bool isVowel(char ch) {
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}

string getClosestVowel(string word) {
    string closestVowel = "";
    for (int i = word.size() - 1; i > 0; i--) {
        if (isVowel(word[i])) {
            if (closestVowel == "") {
                closestVowel = word[i];
            } else {
                return closestVowel;
            }
        }
    }
    return closestVowel;
}

int main() {
    cout << getClosestVowel("yogurt") << endl;
    cout << getClosestVowel("FULL") << endl;
    cout << getClosestVowel("quick") << endl;
    cout << getClosestVowel("ab") << endl;
    return 0;
}
```
C:
```c
#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string getClosestVowel(string word) {
    for (int i = word.size() - 1; i > 0; i--) {
        if (isalpha(word[i]) && isVowel(word[i])) {
            return word[i];
        }
    }
    return "";
}

bool isVowel(char ch) {
    return (ch == 'a' || ch == 'e' || ch