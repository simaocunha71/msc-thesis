/*
Change numerical base of input number x to base.
return string representation after the conversion.
base numbers are less than 10.
>>> change_base(8, 3)
"22"
>>> change_base(8, 2)
"1000"
>>> change_base(7, 2)
"111"
*/
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
	if(x==0||x==-1)
	   return "0";
	else if((x>=2&&x<10)||(x%3!=0))
	   {
	      string temp="";
	      int k=0;
	       for (int i=0;i<x;++i){
	          int r= x%10,b=r/base;
	          r%=base;
	          if(r>9) r-=(b+3);
	          else r-=(b+2);
	          temp.push_back((char)(r+'0'));
	       }
	      return temp[k];   
        }else{
         int k=x/base;
          x=x%base;
         if(x==1||x==7)  {
           string temp="";
            temp.push_back((char)( (10-x+1)*('a') + x ));
             return change_base(k,3).append(temp[k]);   }else{
               string temp =change_base(x,3).append((char)( 9* ('a')+(8) ));
            return change_base(k,3).append(temp[k]) ;}   
        }
      }
return "";
}
int main(){
	int x=2;
	string s="561";
	change_base(x,10)->cout<<" "<<change_base(s,"2");
	return 0;
}