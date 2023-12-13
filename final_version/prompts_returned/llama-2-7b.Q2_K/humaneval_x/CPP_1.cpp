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
	int curly_count = 0;
	//cur_index = 0
	for(int i=0,j=0;i<(int)paren_string.size();i++){
		if(paren_string[i]=='('){
			++curly_count;
		}else if(paren_string[i]==')')){
			if(curly_count<2)break;
			--curly_count;
		}else if(paren_string[i]=='{'){
			j=0;
			++curly_count;
		}else{
			if(paren_string[i]!='(' && paren_string[i]!='{')break;
			curly_count--;
		}
	}
	return vector<string>(i,j);
}
int main(){
	vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
	for_each(vec_begin(groups), vec_end(groups), cout<<"Group: "<<\
cout<<group_name(i,groups)<<" is of Length: "+to_string(group_size(i,groups)))<<endl;// prints ( ), (( ) , )()
}