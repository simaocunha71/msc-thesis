/*
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
    Input: sentence = "This is a test"
    Output: "is"

Example 2:
    Input: sentence = "lets go for swimming"
    Output: "go for"

Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters
*/
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
int i=0,j=0,len=strlen(sentence),k[5];
for(i=1;i<=len/2-1;i++){if(i%2==1)continue;}
while((j<len/2-1||i>=(len)/2-1)){//while j<len/2-1 or i>=(len)/2-1;
        k[0]=i+1;k[1]=' ';k[2]=j+1;k[3]=' ';k[4]=k[0];
        //cout<<k[0]<<" "<<k[1]<<" "<<k[2]<<" "<<k[3]<<" "<<k[4]<<endl;
        if(j>=(len)/2-1)break;
        else{strcpy((sentence)[i],k[0]);if(++i==k[0]+1||(i+1)%2!=1)break;}}
	return sentence;
}
int main(){
freopen("in.txt",_FILEOUT|_S_IWRITE,"wo","utf-8");
int i=6,j=11,k[5];
string s="";for(i=1;i<=6;i++)s+=(i%2!=0?words_in_sentence(i==1?"helloworld":"hello"):" ")+"\n";fprintf(stdout,"%d\