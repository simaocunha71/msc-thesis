```cpp
#include<stdio.h>
#include<string>
using namespace std;
int how_many_times(string str,string substring){
    int count = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str.substr(i, substring.size()) == substring) {
            count++;
        }
    }
    return count;
}
```
