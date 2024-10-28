The syntax of your code seems to be a bit off. I'll provide corrected versions of your code snippets:

Q1:

```cpp
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for  (int i=0; i<numbers.size()-1; i++)
        for  (int j=i+1; j<numbers.size(); j++)
            if  (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}
```

Q2:

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for  (int i=0; i<paren_string.length(); i++)
    {
        chr=paren_string[i];
        if  (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if  (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if  (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}
```

Q