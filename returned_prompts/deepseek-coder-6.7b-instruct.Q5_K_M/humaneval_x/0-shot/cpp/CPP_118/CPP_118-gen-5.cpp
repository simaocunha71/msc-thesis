  int length = word.length();
  string vowels = "aeiouAEIOU";
  for(int i = length-2; i > 0; i--){
    if(vowels.find(word[i]) != string::npos && vowels.find(word[i-1]) == string::npos && vowels.find(word[i+1]) == string::npos){
      return string(1, word[i]);
    }
  }
  return "";
}

int main() {
  printf("%s\n", get_closest_vowel("yogurt").c_str());  // should print "u"
  printf("%s\n", get_closest_vowel("FULL").c_str());   // should print "U"
  printf("%s\n", get_closest_vowel("quick").c_str());  // should print ""
  printf("%s\n", get_closest_vowel("ab").c_str());     // should print ""
  return 0;
}

*/

#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string get_closest_vowel(string word){

  int length = word.length();
  string vowels = "aeiouAEIOU";
  for(int i = length-2; i > 0; i--){
    if(vowels.find(word[i]) != string::npos && vowels.find(word[i-1]) == string::npos && vowels.find(word[i+1]) == string::npos){
      return string(1, word[i]);
    }
  }
  return "";
}

int main() {
  printf("%s\n", get_closest_vowel("yogurt").c_str());  // should print "u"
  printf("%s\n", get_closest_vowel("FULL").c_str());   // should print "U"
  printf("%s\n", get_closest_vowel("quick").c_str());  // should print ""