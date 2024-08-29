#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b[i]+b.substr(0,i);
        if (a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

B:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b.substr(1,b.length()-1)+b[0];
        if (a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

C:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b[i]+b.substr(1,b.length()-1);
        if (a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

D:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b.substr(0,i)+b.substr(i+1,b.length()-1);
        if (a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

E:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b.substr(0,i)+b.substr(i+1,b.length()-1);
        if (a.find(temp)!=string::npos){
            return false;
        }
    }
    return true;
}

F:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b.substr(0,i)+b.substr(i+1,b.length()-1);
        if (a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}

G:
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
    string temp;
    for (int i=0;i<b.length();i++){
        temp=b