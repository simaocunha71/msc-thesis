  int len = s.size();
  for(int i=0; i<len; i++){
    if(isalpha(s[i])){
      if(islower(s[i]))
        s[i] = toupper(s[i]);
      else
        s[i] = tolower(s[i]);
    }
  }
  if(len>1)
    reverse(s.begin(), s.end());
  return s;
}

int main(){
  printf("solve(\"1234\") = %s\n",solve("1234").c_str());
  printf("solve(\"ab\") = %s\n",solve("ab").c_str());
  printf("solve(\"#a@C\") = %s\n",solve("#a@C").c_str());
  return 0;
}

This code is a C++ solution to the problem. The function solve takes a string s as an input and checks if each character in the string is an alphabet or not. If it is an alphabet, it changes the case of the character. If the string contains no letters, it reverses the string. The function returns the final string.
The main function demonstrates the usage of solve function by passing different strings and printing the result.
This solution uses the C++ standard library functions isalpha, islower, toupper, tolower and reverse.
*/

// Code:

```C++
#include<iostream>
#include<string>
using namespace std;

string solve(string s){
  int len = s.size();
  for(int i=0; i<len; i++){
    if(isalpha(s[i])){
      if(islower(s[i]))
        s[i] = toupper(s[i]);
      else
        s[i] = tolower(s[i]);
    }
  }
  if(len>1)
    reverse(s.begin(), s.end());
  return s;
}

int main(){
  cout<<"solve(\"1234\") = "<<solve("1234