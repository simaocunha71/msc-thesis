/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
	if(strings.size()==0) return "";
	string concatStr;
	for(int i=0 ;i<strings.size(); i++){
		concatStr += "\n";
		concatStr+=strings[i];
	}
	return concatStr;
}
//driver code
int main()
{
	vector <string> strings = {"a", "b", "c"};
	concatenate(strings);
	getchar(); getchar(); //for the driver
}
