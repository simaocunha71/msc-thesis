/*
Write a function that takes a string and returns true if the string
length is a prime number or false otherwise
Examples
prime_length("Hello") == true
prime_length("abcdcba") == true
prime_length("kittens") == true
prime_length("orange") == false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool prime_length(string str){
	int count=0,i=0,j=str.length();
	for(i=count+1;i<=str.length();i++){
        if((i%2)==0 && (i<str.length())){
            count+=i;
            str=str+to_string(++count);
        }else{
            str=str+to_string(i);
	    }
}
if(str=="" || count!=1){
    return false;
}else{
return true;}
}
int main(){
printf("Enter String: ");
scanf("%s",str.c_str());
prime_length(str);
return 0;
}
