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
	int x=a.length();
	int y=b.length(); 
	if(x!=y) 
	{
    	cout<<"Invalid Input: Different length of strings"<<endl;
    	return NULL;
    }
    int c[]={0,1};  
	int xc[x],yc[y];
	for(int i=0;i<x;++i) 
	{
		xc[i]=a[i]-'0';
        if (xc[i]==-1) { 
            return NULL;
        }    
    }  
    for(int j=0;j<y;++j) 
    {
      yc[j]=b[j]-'0';
        if (yc[j]==-1) { 
            return NULL;
        }    
    }  
	string res="";
	for(int k=0,i=x-1,j=y-1;k<x+y&&i>=0&&j>=0;++k,++i,++j){
	  int z=(xc[i]+yc[j])%2; //XOR
      	if(z==0)  res+=c[x]='0';    //if xor is same then add '0' to output
        else res+=c[y-1];
      }
	return res;
}
int main(){    
    int i=0,j;
    string a="01",b="01"; 
    while(a.length()!=b.length()) {
        ++i;
        if((++j)%2==1) break;
        a+="0"; //add "0" to make the length of first input equal to second
        b+="