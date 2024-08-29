/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
    Input: sentence = "This is a test"
    Output: "is"

Example 2:
    Input: sentence = "lets go for swimming"
    Output: "go for"

Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters
*/
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string result = "";
    string word = "";
    for(int i = 0; i < sentence.length(); i++){
        if(sentence[i] == ' '){
            if(is_prime(word.length())){
                result += word;
                result += " ";
            }
            word = "";
        } else {
            word += sentence[i];
        }
    }
    if(is_prime(word.length())){
        result += word;
    }
    return result;
}
bool is_prime(int n){
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}
int main(){
    string sentence = "This is a test";
    string output = words_in_sentence(sentence);
    printf("Output: %s\n", output.c_str());
    return 0;
}

C:
/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
    Input: sentence = "This is a test"
    Output: "is"

Example 2:
    Input: sentence = "lets go for swimming"
    Output: "go for"

Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters
*/
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string result = "";
    string word = "";
    bool is_prime = false;
    for(int i = 0; i < sentence.length(); i++){
        if(sentence[i] == ' '){
           