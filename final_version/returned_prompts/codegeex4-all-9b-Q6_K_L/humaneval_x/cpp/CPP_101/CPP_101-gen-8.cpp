#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    stringstream ss(s);
    string word;
    while (ss >> word){
        words.push_back(word);
    }
    return words;
}

B:
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    int i = 0;
    string word;
    while (i < s.size()){
        if (s[i] == ',' || s[i] == ' '){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += s[i];
        }
        i++;
    }
    if (word != ""){
        words.push_back(word);
    }
    return words;
}

C:
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    stringstream ss(s);
    string word;
    while (ss >> word){
        if (word != ""){
            words.push_back(word);
        }
    }
    return words;
}

D:
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    int i = 0;
    string word;
    while (i < s.size()){
        if (s[i] == ',' || s[i] == ' '){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += s[i];
        }
        i++;
    }
    if (word != ""){
        words.push_back(word);
    }
    return words;
}

E:
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    int i = 0;
    string word;
    while (i < s.size()){
        if (s[i] == ',' || s[i] == ' '){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += s[i];
        }
        i++;
    }
    if (word != ""){
        words.push_back(word);
    }
    return words