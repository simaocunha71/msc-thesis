    string vowels = "aeiouAEIOU";
    for (int i = 0; i < vowels.length(); i++){
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}

int main(){
    printf("%s\n",remove_vowels("abcdef\nghijklm").c_str());
    printf("%s\n",remove_vowels("abcdef").c_str());
    printf("%s\n",remove_vowels("aaaaa").c_str());
    printf("%s\n",remove_vowels("aaBAA").c_str());
    printf("%s\n",remove_vowels("zbcd").c_str());
    return 0;
}


A: The string method erase() works by removing elements from the string. The first argument to erase() is an iterator pointing to the first element to be removed, and the second argument is an iterator pointing to the element after the last one to be removed.
In your case, you are using it incorrectly. The function remove() returns an iterator pointing to the new end of the range. You then pass this iterator to erase(), which removes all elements starting from the returned iterator to the end of the string.
Here is the correct way to implement your function:
#include <iostream>
#include <algorithm>
#include <string>

std::string remove_vowels(std::string text){
    std::string vowels = "aeiouAEIOU";
    for (char vowel : vowels) {
        text.erase(std::remove(text.begin(), text.end(), vowel), text.end());
    }
    return text;
}

int main(){
    std::cout << remove_vowels("abcdef\nghijklm") << std::endl;
    std::cout << remove_vowels("abcdef") << std::endl;
    std::cout << remove_vowels("aaaaa") << std::endl;
    std::cout << remove_vowels("aa