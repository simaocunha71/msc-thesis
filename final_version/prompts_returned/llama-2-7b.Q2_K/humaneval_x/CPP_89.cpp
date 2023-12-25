/*
Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
For example:
encrypt("hi") returns "lm"
encrypt("asdfghjkl") returns "ewhjklnop"
encrypt("gf") returns "kj"
encrypt("et") returns "ix"
*/
#include<stdio.h>
#include<string>
using namespace std;
string encrypt(string s){
	int a=0,b=1,c=0,s_length=strlen(s);
	//cout<<a<<endl<<b<<endl<<c<<endl;
	for(int i=0;i<s_length-2;i++){
		if((int)s[i]>9&&((int)s[i])>(10-a)){
			a+=1;
		}else if ((int)s[i]>47&&(int)(s[i]))<=(52-b){
			b+=1;
		}else {c+=1;}
		if(((int)s[i])>(10-a)) a-=1;
		if(((int)s[i])>=(47)&& (52-b)>=47){
			b-=1;
		}
	//cout<<a<<endl<<b<<endl<<c<<endl;
	string t="";t.reserve(strlen(s)+3);
    for(unsigned i = s_length - 2,j=0;i<s_length-1;j++) {
        cout << (char)((a+b+c)%62 + j*48); //48 because it is one less than 'A'.
        t+=char(a+b+c);
    }
    return t;
}
int main()
{
	string s="hello";
	encrypt(s);
return 0;
}