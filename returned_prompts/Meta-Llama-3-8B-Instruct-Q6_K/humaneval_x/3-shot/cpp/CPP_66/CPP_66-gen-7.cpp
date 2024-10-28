    int sum=0;
    for (int i=0;i<s.length();i++)
    {
        if (isupper(s[i]))
        {
            sum+=int(s[i]);
        }
    }
    return sum;
}
```

Here are the answers:

1.

```c
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}
```

2.

```c
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}
```

3.

```c
#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number-int(number);
}
```

4.

```c
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){
    int sum=0;
    for (int i=0;i<s.length();i++)
    {
        if (isupper(s[i]))
        {
            sum+=int(s[i]);
        }
    }
    return sum;
}
```

Let me know if you have any questions about these answers.