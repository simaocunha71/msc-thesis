    vector<string> words;
    vector<string> selected_words;
    string word = "";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            words.push_back(word);
            word="";
        }else{
            word+=s[i];
        }
    }
    words.push_back(word);
    for(int i=0;i<words.size();i++){
        int consonants = 0;
        for(int j=0;j<words[i].length();j++){
            if(words[i][j]=='a'||words[i][j]=='e'||words[i][j]=='i'||words[i][j]=='o'||words[i][j]=='u'){
                continue;
            }else{
                consonants++;
            }
        }
        if(consonants==n){
            selected_words.push_back(words[i]);
        }
    }
    return selected_words;
}
int main(){
    return 0;
}
*/

//Practice/Practice_C++/Questions_C++/Question_12.cpp
#include<iostream>
#include<vector>
#include<string>
using namespace std;

//