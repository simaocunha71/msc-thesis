    // Create a string that contains all the vowels
    string vowels = "aeiouAEIOU";

    // Create a new string that will hold the result
    string result;

    // Loop through each character in the input string
    for(int i = 0; i < text.length(); i++){
        // Check if the character is not in the vowels string
        if(std::find(vowels.begin(), vowels.end(), text[i]) == vowels.end()){
            // If it's not a vowel, add it to the result string
            result += text[i];
        }
    }

    // Return the result
    return result;
}

int main() {
    printf("%s\n", remove_vowels("abcdef\nghijklm").c_str());
    printf("%s\n", remove_vowels("abcdef").c_str());
    printf("%s\n", remove_vowels("aaaaa").c_str());
    printf("%s\n", remove_vowels("aaBAA").c_str());
    printf("%s\n", remove_vowels("zbcd").c_str());
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
    cout << remove_vowels("abcdef\nghijklm") << endl;
    cout << remove_vowels("abcdef") << endl;
    cout << remove_vowels("aaaaa") << endl;
    cout << remove_vowels("aaBAA") << endl;
    cout << remove_vowels("zbcd") << endl;
    return 0;
}
C:
    #include <iostream>
#include <string>
#include <cctype>
using namespace std;

string remove_vowels(string text) {
    string result;

    for (char c : text) {
        if (isalpha(c) && 'a' <= c && c <= 'z' && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            result += c;
        } else if (isalpha(c) && 'A' <= c && c <= 'Z'