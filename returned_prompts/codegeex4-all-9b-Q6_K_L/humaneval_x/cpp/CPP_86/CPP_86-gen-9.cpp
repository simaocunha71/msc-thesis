#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    string w;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            sort(w.begin(),w.end());
            res+=w;
            res+=' ';
            w.clear();
        }
        else{
            w+=s[i];
        }
    }
    sort(w.begin(),w.end());
    res+=w;
    return res;
}

B:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            res+=' ';
        }
        else{
            res+=s[i];
        }
    }
    sort(res.begin(),res.end());
    return res;
}

C:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    for(int i=0;i<s.size();i++){
        if(s[i]!=' '){
            res+=s[i];
        }
    }
    sort(res.begin(),res.end());
    return res;
}

D:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    string w;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            res+=w;
            res+=' ';
            w.clear();
        }
        else{
            w+=s[i];
        }
    }
    res+=w;
    sort(res.begin(),res.end());
    return res;
}

E:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    string w;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            res+=w;
            res+=' ';
            w.clear();
        }
        else{
            w+=s[i];
        }
    }
    sort(w.begin(),w.end());
    res+=w;
    return res;
}

F:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string res;
    for(int i=0;i<s.size();i++){
        if(s[i]!=' '){
            res+=s[i];
        }
    }
    sort(res.begin(),res.end());
    return res;
}

G:
#include<stdio.h>
#include<string