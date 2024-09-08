#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
bool is_happy(string s){
    if(s.size() < 3)
        return false;
    vector<int> counter(26, 0);
    for(char c: s)
        counter[c - 'a']++;
    for(int i = 0; i < 26; i++)
        if(counter[i] > 2)
            return false;
    return true;
}

B:
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
bool is_happy(string s){
    if(s.size() < 3)
        return false;
    vector<int> counter(26, 0);
    for(int i = 0; i < 26; i++)
        for(char c: s)
            counter[c - 'a']++;
    for(int i = 0; i < 26; i++)
        if(counter[i] > 2)
            return false;
    return true;
}

C:
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
bool is_happy(string s){
    if(s.size() < 3)
        return false;
    vector<int> counter(26, 0);
    for(int i = 0; i < 26; i++)
        if(counter[i] > 2)
            return false;
    for(char c: s)
        counter[c - 'a']++;
    return true;
}

D:
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
bool is_happy(string s){
    if(s.size() < 3)
        return false;
    vector<int> counter(26, 0);
    for(char c: s)
        counter[c - 'a']++;
    for(int i = 0; i < 26; i++)
        if(counter[i] > 2)
            return false;
    return true;
}
翻译成中文：
