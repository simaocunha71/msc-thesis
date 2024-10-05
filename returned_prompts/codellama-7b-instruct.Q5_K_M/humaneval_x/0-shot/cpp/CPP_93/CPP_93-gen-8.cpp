/*
Write a function that takes a message, and encodes it in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the english alphabet. 
Assume only letters. 

Examples:
>>> encode('test")
"TGST"
>>> encode("This is a message")
'tHKS KS C MGSSCGG"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){

  //TODO: Your code goes here
  //vowels
  string vowels = "aeiouAEIOU";
  string vowels2;
  string vowels3;
  //char vowels4;
  //int i = 0;
  //char vowels2 = 'a';
  //char vowels3 = 'b';
  for(int i = 0; i < vowels.size(); i++){
    vowels2 += vowels[i];
    vowels3 += vowels[i+2];
  }

  string res = "";
  for(int i = 0; i < message.size(); i++){
    if(message[i] == ' '){
      res += ' ';
    }
    else if(message[i] == ' '){
      res += message[i];
    }
    else if(vowels.find(message[i]) != vowels.npos){
      res += vowels3[i];
    }
    else if(vowels2.find(message[i]) != vowels2.npos){
      res += vowels2[i];
    }
    else if(vowels3.find(message[i]) != vowels3.npos){
      res += vowels[i];
    }
    else{
      res += tolower(message[i]);
    }
  }
  return res;
}

int main(){
  string message = "test";
