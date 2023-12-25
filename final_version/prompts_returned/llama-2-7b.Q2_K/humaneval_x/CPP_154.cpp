/*
You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
cycpattern_check("abcd","abd") => false
cycpattern_check("hello","ell") => true
cycpattern_check("whassup","psus") => false
cycpattern_check("abab","baa") => true
cycpattern_check("efef","eeff") => false
cycpattern_check("himenss",'simen") => true

*/
#include<stdio.h>
#include<string>
using namespace std;
bool cycpattern_check(string a,string b){
	int j=0;
	for(int i=1;i<a.length();i++){
	    if(b[j] == a[i]){
	        //printf("%s",a);
            j++;
         }else {
            break;
          }
       }
	if (strcmp(a, b)==0){
      printf("Cycled word found\n");
	return true;}
     return false;
}
int main(){
    char str1[256]; //char is just to store the string.
   scanf("%s",str1);  //Enter a string here
    int j=0;
    for(int i=1;i<strlen(str1);++i) {
        if(j==strlen(str1)-1){ break;}
      strcpy(a,str1[i]);  //stores the current character in a variable. 
     for (int x = j+1 ;x<=j+2; ++x)    /*checks if there's any substring of length two between the two*/
       {	if(!strcmp(a, str1[i]))     //if current character equals to substring
      printf("%c", a);                        return 0;}//returns 0 if a is not found.
    }
}
