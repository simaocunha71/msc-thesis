```c++
#include<string>
using namespace std;
bool is_palindrome(string text){
    int i = 0;
    int j = text.size() - 1;
    while(i < j) {
        if(text[i] != text[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
```

