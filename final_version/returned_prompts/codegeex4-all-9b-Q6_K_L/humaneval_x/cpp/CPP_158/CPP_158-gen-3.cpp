/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string'}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){

    string max_word = "";
    int max_unique_chars = 0;
    for(int i = 0; i < words.size(); i++){
        int unique_chars = 0;
        for(int j = 0; j < words[i].length(); j++){
            char c = words[i][j];
            bool is_unique = true;
            for(int k = 0; k < j; k++){
                if(words[i][k] == c){
                    is_unique = false;
                    break;
                }
            }
            if(is_unique){
                unique_chars++;
            }
        }
        if(unique_chars > max_unique_chars || (unique_chars == max_unique_chars && words[i] < max_word)){
            max_unique_chars = unique_chars;
            max_word = words[i];
        }
    }
    return max_word;
}

int main(){
    vector<string> words = {"name", "of", 'string'};
    string max_word = find_max(words);
    printf("The word with maximum number of unique characters is: %s\n", max_word.c_str());
    return 0;
}
B:
/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string'}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){

    string max_word = "";
    int max_unique_chars = 0;
    for(int i = 0; i < words.size(); i++){
        int unique