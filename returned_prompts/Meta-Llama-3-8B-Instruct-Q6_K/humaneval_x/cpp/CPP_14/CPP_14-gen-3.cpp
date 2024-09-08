    vector<string> result;
    for(int i=1;i<=str.length();i++){
        result.push_back(str.substr(0,i));
    }
    return result;
}
int main(){
    string s = "abc";
    vector<string> res = all_prefixes(s);
    for(auto i:res){
        printf("%s\n",i.c_str());
    }
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "abc";
    int i, len = strlen(s);
    for(i = 0; i <= len; i++) {
        printf("%.*s\n", i, s);
    }
    return 0;
}

Python:
def all_prefixes(s):
    return [s[:i+1] for i in range(len(s)+1)]

s = "abc"
for prefix in all_prefixes(s):
    print(prefix)  # Output: a, ab, abc
```



## 7.  Write a Python program to find the sum of all the elements in a given list of lists.

