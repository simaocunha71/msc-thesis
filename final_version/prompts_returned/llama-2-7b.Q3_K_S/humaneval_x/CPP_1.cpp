/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "(()())"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
	int paren_count = 0;
	vector<char> temp_vec;
	string group;
	char ch=' ';
	int j=0,k=0,l=0,m=0;
	for(unsigned int i=0 ; i < paren_string.size();i++){
		if(paren_count==1 && paren_count!=j) group = "";
		else if(i!=(paren_string.size()-1))group += ch;
		ch = paren_string[i];
		//printf("%c\n",ch);
		if(ch == '('){
			j++;
		}else if(ch==')' && j!=0)temp_vec.push_back((unsigned int)(paren_count));
		else{
			k+=1; //k contains count of open brackets, it is incremented here for each "(" in input string.
		}
		paren_count++; if(i == (paren_string.size()-2)){
			l += k - paren_count ; group = ""; m+=l;
			k=0; l=0; j=j+m; paren_count = 0; temp_vec.clear(); for(unsigned int i = (j-1); i < j;i++){
			group += ch; ch = paren_string[i]; if(ch == '('){paren_count++;}else{k+=1;}
		}}
		if(i!=0