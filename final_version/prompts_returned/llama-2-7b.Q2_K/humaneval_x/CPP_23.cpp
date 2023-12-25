/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
	int len=0;
	for (int i = 0 ; i <= str.length() ; ++i)
	{
	   if ((str[i] > 'z') && (str[i] < 'a'))
      {
         len +=1; break;
      }
     else if((str[i])>='a'&&(str[i])<='z')
      {
          len +=1;break;
       }
    }   return len;
}
int main(){
string str="hello";
cout<<strlen(str)<<endl;
return 0;
}
