    transform(text.begin(), text.end(),text.begin(), ::tolower);
    int i=0;
B:
    if(i<text.length()){
        if(text[i]=='a' || text[i]=='e' || text[i]=='i' || text[i]=='o' || text[i]=='u'){
            text.erase(i,1);
        }
        else{
            i++;
            goto B;
        }
        goto B;
    }
    return text;
}


A: I'm assuming you want to remove both uppercase and lowercase vowels.
In the original code, you've only checked for lowercase vowels.
To solve this problem, you can convert the whole text to lowercase using the transform() function, so that you can check for both uppercase and lowercase vowels.

A: Here is the C++ solution using the built-in std::remove_if and std::erase_if function from the algorithm library.
The std::remove_if function in C++ is used to remove all the elements in the range [first, last) for which the predicate pred returns true.
The std::erase_if function in C++ is used to remove all the elements in the range [first, last) for which the predicate pred returns true.
#include <algorithm>
#include <iostream>
#include <cctype>

std::string remove_vowels(std::string text)
{
    text.erase(std::remove_if(text.begin(), text.end(), [](unsigned char const c) { return std::string("aeiouAEIOU").find(c) != std::string::npos; }), text.end());
    return text;
}

In this solution, the lambda function checks if the character is a vowel (either lowercase or uppercase). If it is, std::remove_if function removes it. The erase-remove idiom is used to remove the elements from the string.
Example Usage:
int main()
{
    std::cout << remove_vowels("abcdef\nghijklm") << std