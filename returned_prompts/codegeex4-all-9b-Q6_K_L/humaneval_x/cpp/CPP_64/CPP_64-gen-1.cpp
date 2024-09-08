#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int vowels_count(string s){
    int count=0;
    string vowel="AEIOUaeiou";
    for(int i=0;i<s.length();i++){
        if(find(vowel.begin(),vowel.end(),s[i])!=vowel.end()){
            count+=1;
        }
    }
    if(s[s.length()-1]=='y' || s[s.length()-1]=='Y'){
        count+=1;
    }
    return count;
}
int main(){
    string s;
    cin>>s;
    cout<<vowels_count(s)<<endl;
    return 0;
}