    string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] != 'a' && text[i] != 'e' && text[i] != 'i' && text[i] != 'o' && text[i] != 'u' && text[i] != 'A' && text[i] != 'E' && text[i] != 'I' && text[i] != 'O' && text[i] != 'U'){
            result += text[i];
        }
    }
    return result;
}

int main(){
    string str = "abcdef\nghijklm";
    string result = remove_vowels(str);
    cout << result << endl;
    return 0;
}

B:
The problem is asking to create a function that takes a string as an input and returns a new string with all the vowels removed. The function should be able to handle strings with both lowercase and uppercase letters.

Here is a solution for the problem:

```cpp
#include <iostream>
#include <string>
#include <cctype>

std::string remove_vowels(const std::string& str) {
    std::string result;
    for (char c : str) {
        if (!std::isspace(c) && !std::isvowel(c)) {
            result += c;
        }
    }
    return result;
}

bool isvowel(char c) {
    c = std::tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    std::string str = "abcdef\nghijklm";
    std::string result = remove_vowels(str);
    std::cout << result << std::endl;
    return 0;
}
```

In this solution, the `remove_vowels` function iterates over each character in the input string. If the character is not a space and not a vowel (checked using the `isvowel` function), it is added to the result string. The `isvowel` function checks if a character is a vowel by converting it to lowercase and then checking if it is one of the five vowels.

The `main` function demonstrates how to use the `remove_vowels` function by removing vowels from the string "abcdef\nghijklm". The result is then printed to the console.