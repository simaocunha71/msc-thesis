    transform(text.begin(), text.end(), text.begin(), ::tolower);
    string vowels = "aeiou";
    for (int i = 0; i < vowels.size(); i++){
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}

int main() {
    printf("%s\n", remove_vowels("abcdef").c_str());
    printf("%s\n", remove_vowels("aaaaa").c_str());
    printf("%s\n", remove_vowels("aaBAA").c_str());
    printf("%s\n", remove_vowels("zbcd").c_str());
}



A: In the remove_vowels function, you don't need to convert the string to lower case. You can just check for the vowels in uppercase. The tolower function is unnecessary.
string remove_vowels(string text){
    string vowels = "aeiouAEIOU";
    for (int i = 0; i < vowels.size(); i++){
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}

int main() {
    printf("%s\n", remove_vowels("abcdef").c_str());
    printf("%s\n", remove_vowels("aaaaa").c_str());
    printf("%s\n", remove_vowels("aaBAA").c_str());
    printf("%s\n", remove_vowels("zbcd").c_str());
}

This will work fine. The function remove_vowels removes all occurrences of vowels (both uppercase and lowercase) from the given string.

A: Here is a more efficient approach using standard library functions. 
#include <algorithm>
#include <cctype>

std::string remove_vowels(std::string str) {
    str.erase(std::remove_if(str.begin(), str.end(), [](char c) {