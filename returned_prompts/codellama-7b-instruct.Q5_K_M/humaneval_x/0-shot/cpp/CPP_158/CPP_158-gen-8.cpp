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

    vector<string>::iterator it;
    for(it = words.begin(); it != words.end(); it++){
        int count = 0;
        count = unique((*it).begin(),(*it).end());
        if(count > max_count)
            max_count = count;
            max_string = *it;
    }
    return max_string;
}

int main(){
    vector<string> words = {"name", "of", "string"};
    string max_string = find_max(words);
    cout << max_string << endl;
    return 0;
}


