    int i,j;
    string word = "";
    for(i = 0; i < s.length(); i++){
        word = "";
        for(j = i; j < s.length(); j++){
            if(s[j] == ' '){
                sort(word.begin(), word.end());
                s.replace(i, word.length(), word);
                i += word.length();
                break;
            }
            word += s[j];
        }
        if(j == s.length()){
            sort(word.begin(), word.end());
            s.replace(i, word.length(), word);
            break;
        }
    }
    return s;
}

int main() {
    printf("%s\n", anti_shuffle("Hello World!!!").c_str());
    return 0;
}
*/

Output:
Hello  !!!Wdlor

*/


A: In this problem, you are asked to sort each word in a string in ascending order according to their ASCII values. You also need to keep the order of the words and the spaces intact. This can be solved by using a C++ function.

Here is a C++ solution for your problem.

```cpp
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string anti_shuffle(string s) {
    int start = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ' || i == s.length() - 1) {
            if (i == s.length() - 1) i++;
            string subStr = s.substr(start, i - start);
            sort(subStr.begin(), subStr.end());
            s.replace(start, i - start, subStr);
            start = i + 1;
        }
    }
    return s;
}

int main() {
    string s = "Hello World!!!";
    cout << anti_shuffle(s) << endl;
    return 0;
}
```

This program takes