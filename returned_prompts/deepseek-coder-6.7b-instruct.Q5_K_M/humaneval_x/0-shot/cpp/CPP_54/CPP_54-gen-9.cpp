    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0 == s1;
}

int main(){
    printf(same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") ? "true\n" : "false\n");
    printf(same_chars("abcd", "dddddddabc") ? "true\n" : "false\n");
    printf(same_chars("dddddddabc", "abcd") ? "true\n" : "false\n");
    printf(same_chars("eabcd", "dddddddabc") ? "true\n" : "false\n");
    printf(same_chars("abcd", "dddddddabce") ? "true\n" : "false\n");
    printf(same_chars("eabcdzzzz", "dddzzzzzzzddddabc") ? "true\n" : "false\n");
    return 0;
}


A: Here is the C++ code which checks if two words have the same characters:

```cpp
#include<bits/stdc++.h>
using namespace std;

bool same_chars(string s1,string s2)
{
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
}

int main()
{
    cout<<same_chars("eabcdzzzz", "dddzzzzzzzddeddabc")<<"\n";
    cout<<same_chars("abcd", "dddddddabc")<<"\n";
    cout<<same_chars("dddddddabc", "abcd")<<"\n";
    cout<<same_chars("eabcd", "dddddddabc")<<"\n";
    cout<<same_chars("abcd", "dddddddabce")<<"\n";
    cout<<same_chars("eabcdzzzz", "dddzzzzzzz