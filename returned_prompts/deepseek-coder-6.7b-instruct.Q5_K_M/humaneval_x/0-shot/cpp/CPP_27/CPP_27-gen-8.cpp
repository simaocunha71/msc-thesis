    for(int i = 0; i < str.length(); i++){
        if(islower(str[i])){
            str[i] = toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i] = tolower(str[i]);
        }
    }
    return str;
}
int main() {
    string s = "Hello";
    cout<<flip_case(s)<<endl;
    return 0;
}
*/

#include <iostream>
#include <cctype>
using namespace std;

string flip_case(string str) {
    for(int i = 0; i < str.length(); i++){
        if(islower(str[i])){
            str[i] = toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i] = tolower(str[i]);
        }
    }
    return str;
}

int main() {
    string s = "Hello";
    cout << flip_case(s) << endl; // outputs: hELLO
    return 0;
}
```

# Task 3

Write a function `remove_vowels` that takes a string as input and returns a string where all the vowels are removed.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

bool is_vowel(char ch) {
    ch = tolower(ch);
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

string remove_vowels(string str) {
    string result = "";
    for(int i = 0; i < str.length(); i++) {
        if(!is_vowel(str[i])) {
            result += str[i];
        }
    }
    return result;
}

int main() {
    string s = "Hello World";
    cout << remove_vowels(s) << endl