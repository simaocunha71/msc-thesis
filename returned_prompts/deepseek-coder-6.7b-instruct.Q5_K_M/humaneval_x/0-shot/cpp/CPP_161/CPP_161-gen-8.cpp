  string result="";
  for(int i=0; i<s.size(); i++){
    if(isalpha(s[i])){
      if(islower(s[i])){
        result += toupper(s[i]);
      }
      else{
        result += tolower(s[i]);
      }
    }
    else{
      result = s[i]+result;
    }
  }
  return result;
}
int main(){
  printf("%s\n", solve("1234").c_str());
  printf("%s\n", solve("ab").c_str());
  printf("%s\n", solve("#a@C").c_str());
}

//solve.cpp
/*
You are given a string s.
if s[i] is a letter, reverse its case from lower to upper or vise versa, 
otherwise keep it as it is.
If the string contains no letters, reverse the string.
The function should return the resulted string.
Examples
solve("1234") = “4321”
solve("ab") = “AB”
solve("#a@C") = “#A@c”
*/
#include <stdio.h>
#include <string>
using namespace std;
string solve(string s){
  string result="";
  for(int i=0; i<s.size(); i++){
    if(isalpha(s[i])){
      if(islower(s[i])){
        result += toupper(s[i]);
      }
      else{
        result += tolower(s[i]);
      }
    }
    else{
      result = s[i]+result;
    }
  }
  return result;
}
int main(){
  printf("%s\n", solve("1234").c_str());
  printf("%s\n", solve("ab").c_str());
  printf("%s\n", solve("#a@C").c_str());
}

//solve_main.cpp
#include <stdio.h>
#include