/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string filp_case(string str){
	int len=str.length();
	for (int i = 0;i < len ;i++) {
   if (islower((unsigned int)toupper(str[i]))) {
      str[i]=tolower(str[i]);
    } else {
      str[i]=toupper(str[i]);
    }
  }
}
int main(){
	int i;
	string s="Hello";
	for (i = 0; i < len ;i++) {
   if (islower((unsigned int)toupper(str[i]))) {
      str[i]=tolower(str[i]);
    } else {
      str[i]=toupper(str[i]);
    }
  }
}
