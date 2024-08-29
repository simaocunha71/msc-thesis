#include <iostream>
#include <string>
using namespace std;

int digitSum(string s)
{
    int sum = 0;
    for (char c : s)
    {
        if (isupper(c))
        {
            sum += int(c);
        }
    }
    return sum;
}

int main()
{
    string s;
    cin >> s;
    cout << digitSum(s) << endl;
    return 0;
}

C:
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){

    int sum = 0;
    for (int i = 0; i < s.size(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}

D:
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){

    int sum = 0;
    for (int i = 0; i < s.size(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}

E:
#include <iostream>
#include <string>
using namespace std;

int digitSum(string s)
{
    int sum = 0;
    for (char c : s)
    {
        if (isupper(c))
        {
            sum += c;
        }
    }
    return sum;
}

int main()
{
    string s;
    cin >> s;
    cout << digitSum(s) << endl;
    return 0;
}

F:
#include <iostream>
#include <string>
using namespace std;

int digitSum(string s)
{
    int sum = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (isupper(s[i]))
        {
            sum += s[i];
        }
    }
    return sum;
}

int main()
{
    string s;
    cin >> s;
    cout << digitSum(s) << endl;
    return 0;
}

The correct answer is D:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){

    int sum = 0;
    for (int i = 0; i < s.size(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}
```

This solution correctly iterates over each character in the string, checks if it is uppercase, and if it is, adds its ASCII value