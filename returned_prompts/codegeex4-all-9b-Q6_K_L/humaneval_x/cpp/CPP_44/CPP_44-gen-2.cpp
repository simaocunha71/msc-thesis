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
    string result = "";
    while(x > 0){
        result = to_string(x % base) + result;
        x = x / base;
    }
    return result;
}
B:
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
    string result = "";
    while(x > 0){
        result = to_string(x % base) + result;
        x = x / base;
    }
    if(result == ""){
        result = "0";
    }
    return result;
}
C:
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
    string result = "";
    if(x == 0){
        result = "0";
    }
    while(x > 0){
        result = to_string(x % base) + result;
        x = x / base;
    }
    return result;
}
D:
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
    string result = "";
    while(x > 0){
        result = to_string(x % base) + result;
        x = x / base;
   