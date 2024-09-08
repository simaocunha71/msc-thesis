#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string str="";
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            sort(temp.begin(),temp.end());
            str+=temp;
            str+=" ";
            temp="";
        }
        else
        temp+=s[i];
    }
    if(temp!=""){
        sort(temp.begin(),temp.end());
        str+=temp;
    }
    return str;
}
C:
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string str="";
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            sort(temp.begin(),temp.end());
            str+=temp;
            str+=" ";
            temp="";
        }
        else
        temp+=s[i];
    }
    if(temp!=""){
        sort(temp.begin(),temp.end());
        str+=temp;
    }
    return str;
}
D:
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string str="";
    string temp="";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            sort(temp.begin(),temp.end());
            str+=temp;
            str+=" ";
            temp="";
        }
        else
        temp+=s[i];
    }
    if(temp!=""){
        sort(temp.begin(),temp.end());
        str+=temp;
    }
    return str;
}