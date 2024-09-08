#include <iostream>
#include <string>
using namespace std;
string string_xor(string a,string b){
    string c;
    for(int i=0;i<a.length();i++)
    {
        if(a[i]==b[i])
            c+='0';
        else
            c+='1';
    }
    return c;
}