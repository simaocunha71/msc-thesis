/*
Return vector of all prefixes from shortest to longest of the input string
>>> all_prefixes("abc")
{"a", "ab", "abc"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> all_prefixes(string str){
	int n=str.size();
	vector<string> ans(n-1);
	for(int i=2;i<=n;i++){
		if(!isalpha(str[0]))break;
		string prefix = "";
		for(int j=0;j<i;j++)prefix+=str.at(j);
		//printf("%s\n",prefix.c_str());
		ans.push_back(prefix);
	}
	return ans;
}
void print_all_prefixes(vector<string> prefix,int i){
	for(int j=0;j<i;j++){
		printf("%s",prefix[j].c_str());
		if(j!=i-1)printf(" ");
	}
	printf("\n");
}
void print_all_prefixes(vector<string> prefix){
	print_all_prefixes(prefix,prefix.size()-1);
}
int main(){
	string str="abcdefgh";
	vector<string> ans=all_prefixes(str);
	for(int i=0;i<=ans.size();i++){
		print_all_prefixes(ans,i);
	}
	return 0;
}