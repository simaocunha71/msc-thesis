	if(brackets.size()==0)
		return true;
	if(brackets[0]=='<')
		return false;
	int count=0;
	for(int i=0;i<brackets.size();i++)
		if(brackets[i]=='<')
			count++;
	if(count%2==1)
		return false;
	for(int i=0;i<brackets.size();i++)
		if(brackets[i]=='>')
			count--;
	if(count==0)
		return true;
	return false;
}
int main(){
	string brackets;
	cin>>brackets;
	cout<<correct_bracketing(brackets);
}

Ans:

The above solution is correct but it has a time complexity of O(n^2) as it has two nested loops.
A better solution would be to use a stack to keep track of the opening brackets and then compare the contents of the stack with the closing brackets.

#include<stdio.h>
#include<string>
#include<stack>
using namespace std;
bool correct_bracketing(string brackets){
	stack<char> s;
	for(int i=0;i<brackets.size();i++){
		if(brackets[i]=='<')
			s.push(brackets[i]);
		else if(s.size()==0)
			return false;
		else{
			if(s.top()==brackets[i])
				s.pop();
			else
				return false;
		}
	}
	return s.size()==0;
}
int main(){
	string brackets;
	cin>>brackets;
	cout<<correct_bracketing(brackets);
}
