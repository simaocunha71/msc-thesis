#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
    int max_unique = 0;
    string max_string = "";
    for (int i = 0; i < words.size(); i++) {
        int unique_chars = 0;
        vector<char> unique;
        for (int j = 0; j < words[i].size(); j++) {
            if (find(unique