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
    string output="";
    for (int i=0 ;i<=sentence.length()-1;i++) {
        if(!isdigit(sentence[i])){
            output+=sentence[i];
        }else{
            int j = 0;
            while(isdigit(sentence[j])&& j<sentence.length()){
                j++;
            }
            for (int k=1 ;k<=j;k++){
                output+=to_string(k);
            }
        }
    }
    return output;
}