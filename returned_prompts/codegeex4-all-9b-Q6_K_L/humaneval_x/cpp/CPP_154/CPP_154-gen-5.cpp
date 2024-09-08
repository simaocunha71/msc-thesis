#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;
bool cycpattern_check(string a,string b){
    int len = b.length();
    for(int i=0;i<len;i++){
        string temp;
        temp = b.substr(i,len);
        temp += b.substr(0,i);
        if(a.find(temp) != string::npos)
            return true;
    }
    return false;
}
