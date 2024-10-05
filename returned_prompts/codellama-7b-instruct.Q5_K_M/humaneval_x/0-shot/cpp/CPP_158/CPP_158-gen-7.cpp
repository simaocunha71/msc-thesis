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
    vector<string>::iterator max;
    vector<string>::iterator it;
    int max_num = 0;
    for(it = words.begin(); it != words.end(); it++)
    {
        int count = 0;
        string word = *it;
        for(int i = 0; i < word.size(); i++)
        {
            bool flag = false;
            for(int j = 0; j < word.size(); j++)
            {
                if(i != j && word[i] == word[j])
                {
                    flag = true;
                    break;
                }
            }
            if(!flag)
            {
                count++;
            }
        }
        if(count > max_num)
        {
            max = it;
            max_num = count;
        }
    }
    return *max;
}

int main()
{
    vector<string> words;
    words.push_back("name");
    words.push_back("of");
    words.push_back("string");
    string result = find_max(words);
    printf("%s", result.c_str());
    return 0;
}




















