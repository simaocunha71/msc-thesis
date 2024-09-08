    // your code here

    return true/false;
}

int main() {
    string s;
    cin >> s;
    if(is_happy(s)) printf("True\n");
    else printf("False\n");
    return 0;
}

Solution:
Here is a possible solution in C++:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
bool is_happy(string s){
    if(s.length() < 3) return false;
    for(int i=0; i<s.length()-2; i++){
        if(s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2]) return false;
    }
    return true;
}

int main() {
    string s;
    cin >> s;
    if(is_happy(s)) printf("True\n");
    else printf("False\n");
    return 0;
}
```

The idea is to check for each substring of length 3 if all characters are distinct. If we find a substring where the characters are not distinct, we immediately return false. If we have checked all substrings and found no non-distinct substrings, we return true, indicating that the string is happy. If the string is shorter than 3 characters, we return false, as it is not possible for a string of length less than 3 to be happy.

For example, the string "abcd" is happy because it has length 4 and every 3 consecutive letters are distinct ("abc", "bcd", "cde"). On the other hand, the string "aabb" is not happy because it has length 4 and the 3 consecutive letters "aab" are not distinct. The string "adb" is happy because it has length 3 and the 3 consecutive letters are distinct ("ad", "b"). The string "xyy" is not happy because it has length 3 and the 3 consecutive letters are not distinct ("xyy"). The string "a" is not happy because it has length 1 and it is not possible to check for distinctness of 3 consecutive letters. The string "aa" is not happy because it has length 2 and it is not possible to check for distinctness of 3 consecutive letters. The string "abc" is happy because it has length 3 and the 3 consecutive letters are distinct ("abc"). The string "abcd" is happy because it has length 4 and every 3 consecutive letters are