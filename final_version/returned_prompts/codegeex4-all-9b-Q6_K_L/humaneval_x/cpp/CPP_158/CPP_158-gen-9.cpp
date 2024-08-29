#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string find_max(vector<string> words) {
    string max_word = "";
    int max_unique_chars = 0;

    for (string word : words) {
        sort(word.begin(), word.end());
        word.erase(unique(word.begin(), word.end()), word.end());

        if (word.size() > max_unique_chars || (word.size() == max_unique_chars && word < max_word)) {
            max_unique_chars = word.size();
            max_word = word;
        }
    }

    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    string max_word = find_max(words);
    cout << "Max word with unique characters: " << max_word << endl;

    return 0;
}

B:
#include<iostream>
#include<unordered_set>
#include<vector>
#include<string>
using namespace std;
string find_max(vector<string> words){
    string max_word="";
    int max_unique_chars=0;
    for(int i=0;i<words.size();i++){
        unordered_set<char> unique_chars(words[i].begin(),words[i].end());
        if(unique_chars.size()>max_unique_chars||unique_chars.size()==max_unique_chars&&words[i]<max_word){
            max_unique_chars=unique_chars.size();
            max_word=words[i];
        }
    }
    return max_word;
}
int main(){
    vector<string> words={"name","of","string"};
    string max_word=find_max(words);
    cout<<max_word<<endl;
    return 0;
}

C:
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    string max_word="";
    int max_unique_chars=0;
    for(int i=0;i<words.size();i++){
        sort(words[i].begin(),words[i].end());
        words[i].erase(unique(words[i].begin(),words[i].end()),words[i].end());
        if(words[i].size()>max_unique_chars||words[i].size()==max_unique_chars&&words[i]<max_word){
            max_unique_chars=words[i].size();
            max_word=words[i];
        }
    }
    return max_word;
}
int main(){
    vector<string> words={"name","of","string"};
    string max_word=find_max(words);
    cout<<max_word<<endl;
    return 0;
}

D:
#include<iostream