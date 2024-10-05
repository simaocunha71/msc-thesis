    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 97 && str[i] <= 122){
            str[i] = str[i] - 32;
        }else{
            str[i] = str[i] + 32;
        }
    }
    return str;
}
int main(){
    string str = "Hello";
    printf("%s\n",filp_case(str));
    return 0;
}



ANSWER:
/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string flip_case(string str){
    for(int i = 0; i < str.length(); i++){
        if(str[i] >= 97 && str[i] <= 122){
            str[i] = str[i] - 32;
        }else{
            str[i] = str[i] + 32;
        }
    }
    return str;
}
int main(){
    string str = "Hello";
    printf("%s\n",flip_case(str));
    return 0;
}

























































































































































































