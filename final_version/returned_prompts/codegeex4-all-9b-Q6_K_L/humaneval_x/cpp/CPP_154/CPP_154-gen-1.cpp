/*Your answer goes here*/
}
int main(){
    cycpattern_check("abcd","abd");
    cycpattern_check("hello","ell");
    cycpattern_check("whassup","psus");
    cycpattern_check("abab","baa");
    cycpattern_check("efef","eeff");
    cycpattern_check("himenss",'simen');

}
C:
/*
You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
cycpattern_check("abcd","abd") => false
cycpattern_check("hello","ell") => true
cycpattern_check("whassup","psus") => false
cycpattern_check("abab","baa") => true
cycpattern_check("efef","eeff") => false
cycpattern_check("himenss",'simen") => true

*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool cycpattern_check(string a,string b){
    string x=b;
    for(int i=0;i<b.size();i++){
        x=x.substr(1)+x[0];
        if(a.find(x)!=a.npos)
            return true;
    }
    return false;
}
int main(){
    cycpattern_check("abcd","abd");
    cycpattern_check("hello","ell");
    cycpattern_check("whassup","psus");
    cycpattern_check("abab","baa");
    cycpattern_check("efef","eeff");
    cycpattern_check("himenss",'simen');

}