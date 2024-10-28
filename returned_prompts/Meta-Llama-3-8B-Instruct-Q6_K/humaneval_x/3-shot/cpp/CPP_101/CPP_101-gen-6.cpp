    vector<string> words;
    string word;
    for (char c : s)
    {
        if (c==',' || c==' ')
        {
            if (!word.empty())
            {
                words.push_back(word);
                word.clear();
            }
        }
        else
        {
            word+=c;
        }
    }
    if (!word.empty())
    {
        words.push_back(word);
    }
    return words;
} 
// this is a more efficient version of the code
#include<string>
#include<vector>
#include<sstream>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    istringstream iss(s);
    string word;
    while(iss>>word)
    {
        words.push_back(word);
    }
    return words;
}
//this is the most efficient way of doing it
#include<string>
#include<vector>
#include<sstream>
#include<ctype.h>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    istringstream iss(s);
    string word;
    char c;
    while(iss>>c)
    {
        if (!isspace(c))
        {
            word+=c;
        }
        else
        {
            if (!word.empty())
            {
                words.push_back(word);
                word.clear();
            }
        }
    }
    if (!word.empty())
    {
        words.push_back(word);
    }
    return words;
} 
//this is the most efficient way of doing it
#include<string>
#include<vector>
#include<sstream>
#include<ctype.h>
using namespace std;
vector<string> words_string(string s){
    vector<string> words;
    istringstream iss(s);
    string word;
    while(iss>>word)
    {
        words.push_back(word);
    }
    return words;
}
