    int i;
    string result;
    for (i=0;i<a.length();i++)
    {
        if ((a[i]-'0')^ (b[i]-'0'))
            result+=('0'+(a[i]-'0'));
        else
            result+=('0'+(b[i]-'0'));
    }
    return result;
}#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0' && b[i] == '0')
            result += '0';
        else if (a[i] == '1' && b[i] == '1')
            result += '0';
        else
            result += '1';
    }
    return result;
}#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0' && b[i] == '0' || a[i] == '1' && b[i] == '1')
            result += '0';
        else
            result += '1';
    }
    return result;
}#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0' && b[i] == '0' || a[i] == '1' && b[i] == '1')
            result += '0';
        else
            result += '1';
    }
    return result;
}
# include <iostream>
# include <string>
using namespace std;
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if ((a[i] - '0') ^ (b[i] - '0'))
            result += '1';
        else
            result += '0';
    }
    return result;
}
# include <iostream>
# include <string>
using namespace std;
string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == b