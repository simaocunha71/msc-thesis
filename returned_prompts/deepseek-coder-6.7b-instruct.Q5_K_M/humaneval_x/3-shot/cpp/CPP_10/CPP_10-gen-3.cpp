It seems like you are writing C++ code. You should use "std::vector" instead of "vector" and "std::string" instead of "string".

Also, in your C++ codes, you should use "abs()" function instead of "abs()" function in math.h.

Your C++ codes are correct.

The C++ code for the first question is:

```cpp
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for(int i=0;i<numbers.size();i++)
        for(int j=i+1;j<numbers.size();j++)
            if(abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}
```

The C++ code for the second question is:

```cpp
#include<iostream>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for(int i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if(chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if(chr==')')
        {
            level-=1;
            current_paren+=ch