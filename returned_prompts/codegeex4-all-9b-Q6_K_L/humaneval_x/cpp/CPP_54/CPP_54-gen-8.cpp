    //TODO
    return true;
}

int main()
{
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabc"));
    printf("%d\n",same_chars("dddddddabc", "abcd"));
    printf("%d\n",same_chars("eabcd", "dddddddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabce"));
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc"));
    return 0;
}
C:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool same_chars(string s0,string s1){
    int len = s0.size();
    for(int i=0;i<len;i++){
        for(int j=0;j<s1.size();j++){
            if(s0[i]==s1[j]){
                return true;
            }
        }
    }
    return false;
}

int main()
{
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabc"));
    printf("%d\n",same_chars("dddddddabc", "abcd"));
    printf("%d\n",same_chars("eabcd", "dddddddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabce"));
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc"));
    return 0;
}
D:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool same_chars(string s0,string s1){
    int len = s0.size();
    for(int i=0;i<len;i++){
        for(int j=0;j<s1.size();j++){
            if(s0[i]==s1[j]){
                return true;
            }
        }
    }
    return false;
}

int main()
{
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabc"));
    printf("%d\n",same_chars("dddddddabc", "abcd"));
    printf("%d\n",same_chars("eabcd", "dddddddabc"));
    printf("%d\n",same_chars("abcd", "dddddddabce