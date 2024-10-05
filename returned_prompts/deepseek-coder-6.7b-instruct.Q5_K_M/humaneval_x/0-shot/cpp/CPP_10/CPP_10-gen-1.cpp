```cpp
#include<stdio.h>
#include<string>
using namespace std;

bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    int n = str.size();
    if(n==0)
        return "";
    if(is_palindrome(str))
        return str;
    else{
        for(int i=0; i<n; i++){
            if(is_palindrome(str.substr(i))){
                string s(str.rbegin()+i,str.rend());
                return str+string(s.rbegin(),s.rend());
            }
        }
    }
}
```

