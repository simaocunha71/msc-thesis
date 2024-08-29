#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    string res=s;
    for(int i=0;i<s.length();i++){
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                res.erase(i,1);
                i--;
                break;
            }
        }
    }
    if(res==string(res.rbegin(),res.rend())){
        return {res,"True"};
    }
    else{
        return {res,"False"};
    }
}

B:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    string res=s;
    for(int i=0;i<s.length();i++){
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                res.erase(i,1);
                i--;
                break;
            }
        }
    }
    if(res==string(res.rbegin(),res.rend())){
        return {res,"True"};
    }
    else{
        return {res,"False"};
    }
}

C:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    string res=s;
    for(int i=0;i<s.length();i++){
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                res.erase(i,1);
                i--;
                break;
            }
        }
    }
    if(res==string(res.rbegin(),res.rend())){
        return {res,"True"};
    }
    else{
        return {res,"False"};
    }
}

D:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    string res=s;
    for(int i=0;i<s.length();i++){
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                res.erase(i,1);
                i--;
                break;
            }
        }
    }
    if(res==string(res.rbegin(),res.rend())){
        return {res,"True"};
    }
    else{
        return {res,"False"};
    }
}

E:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    string res=s;
