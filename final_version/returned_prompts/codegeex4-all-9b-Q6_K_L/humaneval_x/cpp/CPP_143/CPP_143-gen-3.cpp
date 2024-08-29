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
                result += word + " ";
            }
            word = "";
        }
        else{
            word += sentence[i];
        }
    }
    if(is_prime(word.length())){
        result += word;
    }
    return result;
}
bool is_prime(int num){
    if(num < 2){
        return false;
    }
    for(int i = 2; i < num; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}

B:
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
                result += word + " ";
            }
            word = "";
        }
        else{
            word += sentence[i];
        }
    }
    if(is_prime(word.length())){
        result += word;
