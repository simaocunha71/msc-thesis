    string str;
    for (int i=0;i<=n;i++)
    {
        str+=to_string(i);
        if (i<n)
        str+=" ";
    }
    return str;
}#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string str;
    for (int i=0;i<=n;i++)
    {
        str+=to_string(i);
        if (i<n)
        str+=" ";
    }
    return str;
}
