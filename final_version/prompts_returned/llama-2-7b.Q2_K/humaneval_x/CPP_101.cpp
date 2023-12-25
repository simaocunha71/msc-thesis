/*
You will be given a string of words separated by commas or spaces. Your task is
to split the string into words and return a vector of the words.

For example:
words_string("Hi, my name is John") == {"Hi", "my", "name", "is", "John"}
words_string("One, two, three, four, five, six") == {"One", 'two", 'three", "four", "five", 'six"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
	int n=s.size();
	int i=1,len;
	for(i=n-1;i>=0;--i)
	if((s[i]==','||s[i]==' ')&&(s[i+1]==' ')){
		while(i>=0&&s[i]!=' ')
		len++;
	}else
	len+=2;
	vector<string> res;
	for (int i=0;i<n-1;++i)
	if(((s[i]==','||s[i]==' ')&&(s[i+1]==' '))||s[i]!=' ')
	res.push_back(s.substr(i,len));
	return res;
}
int main(){
	string t="my name is John";
	vector<string> v=words_string(t);
	for (auto w : v) cout<<w<<' ';
	cout<<endl;
	system("pause");
	return 0;
}