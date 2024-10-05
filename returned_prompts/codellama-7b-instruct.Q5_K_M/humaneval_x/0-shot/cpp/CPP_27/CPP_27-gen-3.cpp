/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string filp_case(string str){

string result = "";
for(int i = 0; i < str.size(); i++){
char c = str[i];
if(c >= 'A' && c <= 'Z'){
c = c - 'A' + 'a';
}
else if(c >= 'a' && c <= 'z'){
c = c - 'a' + 'A';
}
result += c;
}
return result;
}
//test code
int main(){
string str = "Hello";
string result = filp_case(str);
cout << result << endl;
return 0;
}
