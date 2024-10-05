#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string>res;
    for (int i = 0; i < s.size(); i++) {
        string str = "";
        while (i < s.size() && s[i] != ' ') {
            str += s[i++];
        }
        if (str.size() == n) {
            bool ok = true;
            for (int j = 0; j < str.size(); j++) {
                if (str[j] != 'a' && str[j] != 'e' && str[j] != 'i' && str[j] != 'o' && str[j] != 'u' && str[j] != 'y') ok = false;
            }
            if (ok) res.push_back(str