vector<string> words;
if(txt.find(' ') != string::npos) {
    string word;
    for(auto x: txt){
        if(x == ' ') {
            words.push_back(word);
            word = "";
        } else {
            word += x;
        }
    }
    words.push_back(word);
}
else if(txt.find(',') != string::npos) {
    string word;
    for(auto x: txt){
        if(x == ',') {
            words.push_back(word);
            word = "";
        } else {
            word += x;
        }
    }
    words.push_back(word);
}
else {
    int count = 0;
    for(auto x: txt){
        if(islower(x) && (x - 'a') % 2 == 1) count++;
    }
    words.push_back(to_string(count));
}
return words;
}

int main() {
  vector<string> words = split_words("Hello,world!");
  for(string word: words) {
    printf("%s\n", word.c_str());
  }
  return 0;
}
*/

I'm not sure how to fix this code. I've tried to solve it by adding a new else if statement to check for commas but it doesn't seem to work. Can you help me fix this code?

A: The issue here is that you're checking for commas and spaces but you're also checking for lower-case letters with odd order in the alphabet. This is causing the program to incorrectly split the string.
You should split the string based on the first occurrence of either a space or a comma. After that, check if the resulting string contains any lowercase letters with odd order in the alphabet.
Here's the corrected code:
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

std::vector<std::string> split_words(std::string txt) {
    std::vector<std::string> words;
   