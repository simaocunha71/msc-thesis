#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s = "hi";
    for(int i=0;i<s.length();i++)
    {
        if(s[i]>=65 && s[i]<=90)
        {
            if(s[i]+4>90)
                s[i] = s[i] + 4 - 26;
            else
                s[i] = s[i] + 4;
        }
        else if(s[i]>=97 && s[i]<=122)
        {
            if(s[i]+4>122)
                s[i] = s[i] + 4 - 26;
            else
                s[i] = s[i] + 4;
        }
    }
    cout<<s;
    return 0;
}

B:
#include<iostream>
#include<string>
using namespace std;
string encrypt(string str)
{
    string encrypted="";
    for(int i=0;i<str.length();i++)
    {
        if(str[i]>=65 && str[i]<=90)
        {
            if(str[i]+4>90)
                encrypted = encrypted + (char)(str[i] + 4 - 26);
            else
                encrypted = encrypted + (char)(str[i] + 4);
        }
        else if(str[i]>=97 && str[i]<=122)
        {
            if(str[i]+4>122)
                encrypted = encrypted + (char)(str[i] + 4 - 26);
            else
                encrypted = encrypted + (char)(str[i] + 4);
        }
        else
            encrypted = encrypted + str[i];
    }
    return encrypted;
}
int main()
{
    string s = "hi";
    cout<<encrypt(s);
    return 0;
}