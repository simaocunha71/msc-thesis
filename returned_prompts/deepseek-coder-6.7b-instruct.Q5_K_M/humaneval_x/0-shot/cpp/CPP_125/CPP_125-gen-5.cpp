    vector<string> vec;

    if(txt.find(' ') != string::npos)
    {
        string word;
        istringstream iss(txt);
        while (iss >> word)
        {
            vec.push_back(word);
        }
        return vec;
    }

    else if(txt.find(',') != string::npos)
    {
        replace(txt.begin(), txt.end(), ',', ' ');
        string word;
        istringstream iss(txt);
        while (iss >> word)
        {
            vec.push_back(word);
        }
        return vec;
    }

    else
    {
        int count = 0;
        for_each(txt.begin(), txt.end(), [&count](char c){
            if(islower(c) && (c - 'a') % 2 != 0)
                ++count;
        });
        vec.push_back(to_string(count));
        return vec;
    }
}

int main()
{
    vector<string> test = split_words("Hello,world!");
    for(int i=0; i<test.size(); i++)
        printf("%s ", test[i].c_str());

    return 0;
}
*/

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

vector<string> split_words(string txt){
    vector<string> words;

    if(txt.find(' ') != string::npos){
        string word;
        istringstream iss(txt);
        while(iss >> word){
            words.push_back(word);
        }
    }
    else if(txt.find(',') != string::npos){
        replace(txt.begin(), txt.end(), ',', ' ');
        string word;
        istringstream iss(txt);
        while(iss >> word){
            words.push_back(word);
        }
    }
    else{
       