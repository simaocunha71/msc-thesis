#include<stdio.h>
#include<math.h>
#include<time.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string> res;
    string word;
    int count=0;
    int i=0;
    while(i<s.length()){
        if(s[i]==' '){
            if(count==n){
                res.push_back(word);
            }
            count=0;
            word="";
        }
        else if(s[i]!=' '){
            word+=s[i];
            if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u'){
                count+=1;
            }
        }
        i++;
    }
    if(count==n){
        res.push_back(word);
    }
    return res;
}
C:
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string> res;
    string word;
    int count=0;
    int i=0;
    while(i<s.length()){
        if(s[i]==' '){
            if(count==n){
                res.push_back(word);
            }
            count=0;
            word="";
        }
        else if(s[i]!=' '){
            word+=s[i];
            if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u'&&s[i]!='A'&&s[i]!='E'&&s[i]!='I'&&s[i]!='O'&&s[i]!='U'){
                count+=1;
            }
        }
        i++;
    }
    if(count==n){
        res.push_back(word);
    }
    return res;
}
D:
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string> res;
    string word;
    int count=0;
    int i=0;
    while(i<s.length()){
        if(s[i]==' '){
            if(count==n){
                res.push_back(word);
            }
            count=0;
            word="";
        }
        else if(s[i]!=' '){
            word+=s[i];
            if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u'&&s[i]!='A'&&s