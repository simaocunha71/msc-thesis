/*
Change numerical base of input number x to base.
return string representation after the conversion.
base numbers are less than 10.
>>> change_base(8, 3)
"22"
>>> change_base(8, 2)
"1000"
>>> change_base(7, 2)
"111"
*/
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){

    string s;
    while(x>0){
        int i=x%base;
        s.insert(s.begin(),i+'0');
        x=x/base;
    }
    return s;

}