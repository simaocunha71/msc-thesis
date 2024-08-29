#include <iostream>
#include <string>
using namespace std;

bool is_vowel(char c){
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
}

string remove_vowels(string text){
    string result = "";
    for (char c : text){
        if (!is_vowel(c)){
            result += c;
        }
    }
    return result;
}

int main(){
    cout << remove_vowels("abcdef\nghijklm") << endl; // "bcdf\nghjklm"
    cout << remove_vowels("abcdef") << endl; // "bcdf"
    cout << remove_vowels("aaaaa") << endl; // ""
    cout << remove_vowels("aaBAA") << endl; // "B"
    cout << remove_vowels("zbcd") << endl; // "zbcd"
    return 0;
}