/*
You are given a string s.
Your task is to check if the string is happy or not.
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
For example:
is_happy("a") => false
is_happy("aa") => false
is_happy("abcd") => true
is_happy("aabb") => false
is_happy("adb") => true
is_happy("xyy") => false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_happy(string s){
	int c=0,count=0;
	if(s==nullptr) return 1;
	else{
		for(auto i:s)
			c++;
	}
	int j=3;
	while(j<c+1){
		string str = s.substr((i-j),j);
		if(str[0]==str[j] || str[0]==str[j+1]|| str[0]==str[j+2]){
			return 0;
		}
		else if(is_happy(str)) return 1;
		count++;
		if((i-j)%3!=0){
			return 0;
		}
		else{
			if(c==s.length() && j==2){
				return 1;
			}
		}
	}
	for(int i=0;i<count/3+1;++i)
		cout<<" ";
	return 0;

}
#ifdef USE_MAIN_DEBUGGER
// To enable debug output, remove line below.
// In the debugger, press "next frame" until you get to a __debugBreak() call and
// the output should be printed there too.
int main(){ }
#endif  // USE_MAIN_DEBUGGER