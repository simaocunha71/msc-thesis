The function `remove_vowels` is not correct. It should return a string without vowels, but you are returning a string with vowels removed twice. The function should be:

```cpp
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

string remove_vowels(string text) {
    string vowels = "aeiouAEIOU";
    for (char vowel : vowels) {
        text.erase(remove(text.begin(), text.end(), vow