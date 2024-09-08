    if(s.length() < 3)
        return false;
    for(int i = 0; i < s.length() - 2; i++){
        if(s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2])
            return false;
    }
    return true;
}

int main(){
    string s;
    printf("Enter a string: ");
    getline(cin, s);
    if(is_happy(s))
        printf("The string is happy\n");
    else
        printf("The string is not happy\n");
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

int is_happy(char s[]) {
    int len = strlen(s);
    if(len < 3)
        return 0;
    for(int i = 0; i < len - 2; i++) {
        if(s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2])
            return 0;
    }
    return 1;
}

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    if(is_happy(s))
        printf("The string is happy\n");
    else
        printf("The string is not happy\n");
    return 0;
}

R:
```python
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True

s = input("Enter a string: ")
if is_happy(s):
    print("The string is happy")
else:
    print("The string is not happy")
```



Solution:
Here is a C++ solution for the problem:
```cpp
#include <iostream>
#include <string>

bool is_happy(std::string s) {
    if (s.length() < 3) {
        return false;
    }
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i+1] || s[i]