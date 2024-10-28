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
    string new_sentence = "";
    string temp = "";
    char space = ' ';
    int length = sentence.size();
    int i = 0;
    int j = 0;
    int k = 0;
    while(i < length){
        if(sentence[i] != space){
            temp = temp + sentence[i];
            i++;
        }
        else{
            k = 0;
            for(int p = 2; p < temp.size(); p++){
                if(temp.size() % p == 0){
                    k = 1;
                    break;
                }
            }
            if(k == 0){
                new_sentence = new_sentence + temp + " ";
            }
            temp = "";
            j++;
        }
    }
    return new_sentence;
}

int main(){
    string sentence = "This is a test";
    string new_sentence = words_in_sentence(sentence);
    printf("%s", new_sentence.c_str());
    return 0;
}
