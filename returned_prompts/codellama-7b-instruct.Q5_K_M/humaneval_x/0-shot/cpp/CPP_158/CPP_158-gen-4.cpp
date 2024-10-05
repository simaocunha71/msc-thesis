/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string"}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    string result = "";
    int max = 0;
    for(int i = 0; i < words.size(); i++){
        if(words[i].length() > max){
            max = words[i].length();
            result = words[i];
        }
        else if(words[i].length() == max){
            if(words[i] < result){
                result = words[i];
            }
        }
    }
    return result;
}
int main(){
    vector<string> words;
    words.push_back("aaaaaaa");
    words.push_back("bb");
    words.push_back("cc");
    cout << find_max(words) << endl;
    return 0;
}


