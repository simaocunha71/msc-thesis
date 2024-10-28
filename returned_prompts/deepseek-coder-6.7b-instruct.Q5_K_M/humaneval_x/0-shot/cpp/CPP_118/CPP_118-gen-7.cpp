  string vowels="aeiouAEIOU";
  for(int i=word.size()-2;i>0;i--){
    if(vowels.find(word[i])==string::npos && vowels.find(word[i-1])==string::npos && vowels.find(word[i+1])==string::npos){
      return string(1,word[i]);
    }
  }
  return "";
}
*/

#include<iostream>
int main(){
  cout<<get_closest_vowel("yogurt")<<endl;
  cout<<get_closest_vowel("FULL")<<endl;
  cout<<get_closest_vowel("quick")<<endl;
  cout<<get_closest_vowel("ab")<<endl;
}

//src/exercises/3.cpp
//
// Created by t-xi on 2020/10/24.
//

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


//