    vector<string> words;
    string word = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' ' || s[i] == ','){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else {
            word += s[i];
        }
    }
    if (word != ""){
        words.push_back(word);
    }
    return words;
}

int main(){
    string s;
    printf("Enter the string:\n");
    getline(cin, s);
    vector<string> words = words_string(s);
    printf("Words:\n");
    for (int i = 0; i < words.size(); i++){
        printf("%s\n", words[i].c_str());
    }
    return 0;
}

This code is written in C++ and it takes a string as input and splits it into words using space and comma as delimiters. It then returns a vector of the words. It also handles cases where there are consecutive delimiters, and it ignores them.
*/

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    string word = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' ' || s[i] == ','){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else {
            word += s[i];
        }
    }
    if (word != ""){
        words.push_back(word);
    }
    return words;
}

int main(){
    string s;
    printf("Enter the string:\n");
    getline(cin, s);
    vector<string> words = words_string(s);
    printf("Words:\n");
    for