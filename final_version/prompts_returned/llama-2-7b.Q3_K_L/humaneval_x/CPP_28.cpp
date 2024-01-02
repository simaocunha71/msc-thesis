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
	return strings[strings.size()-1];
}
int main(){
	vector <string> vec={"a","b","c"};
	printf("%s\n",concatenate(vec));
	return 0;
}
