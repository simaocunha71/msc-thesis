    return "111";
}
int main()
{
    string a="10101010";
    string b="01010101";
    printf("%s",string_xor(a,b).c_str());
    return 0;
}

Ans:
/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    char c[200];
    int i=0,j=0;
    while(a[i]!='\0' && b[j]!='\0'){
        c[i]=a[i]^b[j];
        i++;
        j++;
    }
    c[i]='\0';
    return string(c);
}
int main()
{
    string a="10101010";
    string b="01010101";
    printf("%s",string_xor(a,b).c_str());
    return 0;
}
