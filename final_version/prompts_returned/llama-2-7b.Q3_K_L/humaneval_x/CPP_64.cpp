/*
Write a function vowels_count which takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
Here, 'y' is also a vowel, but only when it is at the end of the given word.
Example: 
>>> vowels_count("abcde") 
2 
>>> vowels_count("ACEDY") 
3
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int vowels_count(string s){
	int v=0,i=0;
	while(!s.empty()){
		if((to_lower(s[0])=='a')|| (to_lower(s[0])=='e')|| (to_lower(s[0])=='i')|| (to_lower(s[0])=='o')|| (to_lower(s[0])=='u'))){
			v=v+1;
		}else{
			for(int j=0;j<s.size();j++){
				if((to_lower(s[j])=='y')&& (i==2)){
					break;
				}else{
					v=v+1;
				}
			}
		}
		if(!s.empty()){
			i++;
			s=s.substr(1,s.size());
		}else{
			break;
		}
	}
	return v;
}
int main(){
	string s="acdedy",t[]={"a","e","i","o","u","y"};
	for(int i=0;i<vowels_count.size();i++){
		printf("%c\n",t[i]);
	}
}