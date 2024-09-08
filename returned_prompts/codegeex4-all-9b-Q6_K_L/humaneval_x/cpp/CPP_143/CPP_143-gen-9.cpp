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
#include<iostream>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string word;
    string result;
    int len;
    int i;
    int j;
    int flag;
    for(i = 0; i < sentence.size(); i++){
        if(sentence[i] == ' '){
            // is a word
            len = word.size();
            if(len == 1) {
                // is prime
                result += word;
                result += ' ';
            }
            else{
                // is not prime
                flag = 0;
                for(j = 2; j < len; j++){
                    if(len % j == 0){
                        flag = 1;
                        break;
                    }
                }
                if(flag == 0){
                    result += word;
                    result += ' ';
                }
            }
            word = "";
        }
        else{
            // is not a word
            word += sentence[i];
        }
    }

    len = word.size();
    if(len == 1) {
        // is prime
        result += word;
        result += ' ';
    }
    else{
        // is not prime
        flag = 0;
        for(j = 2; j < len; j++){
            if(len % j == 0){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            result += word;
            result += ' ';
        }
    }
    return result;
}
int main(){
    string sentence;
    cin >> sentence;
    cout << words_in_sentence(sentence) << endl;
    return 0;
}

B:
/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string