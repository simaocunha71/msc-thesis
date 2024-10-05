  string vowels="aeiouAEIOU";
  for(int i=0;i<message.length();i++){
    if(vowels.find(message[i]) != string::npos){
      if(islower(message[i])){
        message[i] = 'c';
      }
      else{
        message[i] = 'C';
      }
    }
  }
  transform(message.begin(), message.end(), message.begin(), ::toupper);
  return message;
}
*/

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string encode(string message){
  for (int i=0; i<message.size(); i++) {
    if (isalpha(message[i])){
      if (isupper(message[i])){
        message[i] = tolower(message[i]);
      }
      else{
        message[i] = toupper(message[i]);
      }
    }
  }
  for (int i=0; i<message.size(); i++) {
    if (message[i]=='A'){
      message[i] = 'C';
    }
    else if (message[i]=='E'){
      message[i] = 'G';
    }
    else if (message[i]=='I'){
      message[i] = 'K';
    }
    else if (message[i]=='O'){
      message[i] = 'Q';
    }
    else if (message[i]=='U'){
      message[i] = 'W';
    }
    else if (message[i]=='a'){
      message[i] = 'c';
    }
    else if (message[i]=='e'){
      message[i] = 'g';
    }
    else if (message[i]=='i'){
      message[i] = 'k';
    }
    else if (message[i]=='o'){
      message[i] = 'q';
