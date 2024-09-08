

The function `anti_shuffle` takes a string as an input and returns a string where all the words are replaced by a new word where all the characters are arranged in ascending order based on ASCII value.

Here is the C++ code for the function:

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string anti_shuffle(string s) {
    // Separate the words by space
    string words[1000];
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            count++;
        }
    }
    int j = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            words[count] = s.substr(j, i - j);
            j = i + 1;
            count++;
        }
    }
    words[count] = s.substr(j, s.length() - j);

    // Sort the characters in each word
    for(int i = 0; i < count; i++){
        string temp = words[i];
        sort(temp.begin(), temp.end());
        words[i] = temp