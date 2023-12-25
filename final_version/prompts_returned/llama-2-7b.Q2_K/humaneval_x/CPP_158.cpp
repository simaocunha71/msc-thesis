/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string"}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
	int i,j=0;
	for(i = 0 ; i < words.size(); ++i) j += words[i].length(); //calculating length of each element in vector
	sort(words.begin(), words.end());
	if(j == 1) return "word";
	int length;
	for (int i = 0; i < words.size() - 1 ; i++)
    {
        if (words[i].length() < words[i+1].length())
            length = words[i+1].length(); //getting the maximum length of string in vector
        else length = words[i].length();
	}
    return words[length-1];
}
int main(){
    vector<string> v;
    int i,j=0;
for(;;){
    cout<<"Enter word: ";
    string wrd;
    cin>>wrd;
    if(!wrd.compare("word")) break;
	v.push_back(wrd);
}
cout<<"\n\nappended elements in vector: ";
for(int i=0;i<v.size();i++){
    cout<<v[i].c_str()<<" ";
}
cout<<endl;
find_max(v);
return 0;
}