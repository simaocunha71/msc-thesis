/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string flip_case(string str){

    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            str[i]= toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
        else{
            return str;
        }
    }
    return str;
}

int main()
{
    string str = "Hello";
    cout<<flip_case(str)<<endl;
    return 0;
}

B:
/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string flip_case(string str){

    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            str[i]= toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
        else{
            return str;
        }
    }
    return str;
}

int main()
{
    string str = "Hello";
    cout<<flip_case(str)<<endl;
    return 0;
}

C:
/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string flip_case(string str){

    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            str[i]= toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
        else{
            return str;
        }
    }
    return str;
}

int main()
{
    string str = "Hello";
    cout<<flip_case(str)<<endl;
    return 0;
}

D:
/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string flip_case(string str){

    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            str[i]= toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
        else{
            return str;
       