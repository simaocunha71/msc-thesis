/*
Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor("010", "110")
"100"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_xor(string a,string b){
	int len=a.length();
	for(int i=0 ;i<len;i++){
	    if((a[i]) ^ (b[i]))
        printf("%d",a[i]);
    	printf(" ");
    }
}
main()
{
 string_xor("010","110");
 getchar();
 system("pause");
 return 0;
}
