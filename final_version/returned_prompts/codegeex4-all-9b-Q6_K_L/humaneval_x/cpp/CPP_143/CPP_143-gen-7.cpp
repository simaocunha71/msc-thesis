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
#include<vector>
using namespace std;
string words_in_sentence(string sentence){
    string result;
    string temp;
    vector<string> words;
    for(int i = 0; i < sentence.length(); i++){
        if(sentence[i] == ' '){
            words.push_back(temp);
            temp = "";
        }
        else{
            temp = temp + sentence[i];
        }
    }
    words.push_back(temp);
    for(int i = 0; i < words.size(); i++){
        if(is_prime(words[i].length())){
            result = result + words[i] + " ";
        }
    }
    result.pop_back();
    return result;
}
bool is_prime(int n){
    if(n == 2 || n == 3 || n == 5 || n == 7){
        return true;
    }
    else if(n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0){
        return false;
    }
    else{
        return true;
    }
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
#include<vector>
using namespace std;
string words_in_sentence(string sentence){
    string result;
    string temp;
    vector<string> words