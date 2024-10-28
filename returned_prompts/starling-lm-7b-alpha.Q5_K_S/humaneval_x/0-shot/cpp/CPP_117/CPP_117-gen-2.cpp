    vector<string> res;
    for(int i=0;i<s.size();i++)
        if(s[i]>='A'&&s[i]<='Z'||s[i]>='a'&&s[i]<='z'){
            string tmp="";
            while(i<s.size()&&(s[i]>='A'&&s[i]<='Z'||s[i]>='a'&&s[i]<='z'))tmp+=s[i++];
            if(tmp.size()>0)
                if(count_consonant(tmp)==n)res.push_back(tmp);
        }
    return res;
}
int count_consonant(string s){
    int res=0;
    for(int i=0;i<s.size();i++)if(!isvowel(s[i]))res++;
    return res;
}
bool isvowel(char c){
    if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='y'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U'||c=='Y')return 1;
    return 0;
}
int main(){
    string s="Mary had a little lamb";
    vector<string> res=select_words(s,3);
    for(auto it:res)printf("%s\n",it.c_str());
    return 0;
}

*/

/*

#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string> res;
    for(int i=0;i<s.size();i++)
        if(s[i]>='A'&&s[i]<='Z'||s[i]>='a'&&s[i]<='z'){
            string tmp="";
            while(i<s.size