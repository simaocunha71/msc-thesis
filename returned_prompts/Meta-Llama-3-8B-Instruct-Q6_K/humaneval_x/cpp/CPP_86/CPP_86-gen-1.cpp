    string res = "";
    string temp;
    for(int i = 0; i < s.size(); i++){
        if(s[i] != ' '){
            temp += s[i];
        }else{
            sort(temp.begin(), temp.end());
            res += temp + " ";
            temp = "";
        }
    }
    sort(temp.begin(), temp.end());
    res += temp;
    return res;
} 

C++ code to solve the problem. The function `anti_shuffle` takes a string as input and returns an ordered version of it. The ordered version is created by replacing each word in the string with a new word where all the characters are arranged in ascending order based on ASCII value. The order of words and blank spaces in the sentence is maintained.

The function works by iterating over the input string. If the current character is not a space, it is added to a temporary string. If the current character is a space, the temporary string is sorted in ascending order and added to the result string. The process is repeated for each word in the string. Finally, the last word is sorted and added to the result string.

The time complexity of the function is O(n*m*logm), where n is the length of the input string and m is the maximum length of a word in the string. The space complexity is O(n*m), where n is the length of the input string and m is the maximum length of a word in the string.

Here is the C++ code:

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string anti_shuffle(string s) {
    string res = "";
    string temp;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != ' ') {
            temp += s[i];
        } else {
            sort(temp.begin(), temp.end());
            res += temp + " ";
            temp = "";
        }
    }
    sort(temp.begin(), temp.end());
    res += temp;
    return res;
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    cout << "Ordered version: " << anti_shuffle(s) << endl;
    return 0;
}
```

In this code, the `anti_shuffle` function is defined to take a string as input and return an ordered version of it. The `main` function is used to test the `anti_shuffle` function. It prompts the user to enter a string