/*
You'll be given a string of words, and your task is to count the number
of boredoms. A boredom is a sentence that starts with the word "I".
Sentences are delimited by '.', '?' or '!'.

For example:
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
*/
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){
	int counter=0;
	for(int i=0;i!=S.size();++i)
	{
		if(S[i].compare('?')==0 && (S[i+1].compare('!')==0 || S[i+1].compare('.') == 0))
		counter+=2;
		else if(S[i].compare('!')==0)
		counter++;
	}
return counter;}
int main(){
	string s;
    cout<<"Enter a sentence: ";
	cin>>s;
	cout<<is_bored(s);
	system("pause");
    return 0;
}