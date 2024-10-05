    transform(text.begin(), text.end(), text.begin(), ::tolower);
    int i = 0;
B:
    if(i < text.size()){
        if(text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u'){
            text.erase(i, 1);
        } else {
            i++;
            goto B;
        }
        goto B;
    }
C:
    return text;
}

int main() {
    printf("%s\n", remove_vowels("abcdef\nghijklm").c_str());
    printf("%s\n", remove_vowels("abcdef").c_str());
    printf("%s\n", remove_vowels("aaaaa").c_str());
    printf("%s\n", remove_vowels("aaBAA").c_str());
    printf("%s\n", remove_vowels("zbcd").c_str());
    return 0;
}

*/


A: You're using Goto statements incorrectly. Goto statements are used to jump to another part of your code. It's not a control flow tool like if, else or switch.
Here is a correct version of your code:

```c++
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string remove_vowels(string