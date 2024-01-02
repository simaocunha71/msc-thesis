/*
In this task, you will be given a string that represents a number of apples and oranges 
that are distributed in a basket of fruit this basket contains 
apples, oranges, and mango fruits. Given the string that represents the total number of 
the oranges and apples and an integer that represent the total number of the fruits 
in the basket return the number of the mango fruits in the basket.
for example:
fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
*/
#include<stdio.h>
#include<string>
using namespace std;
int fruit_distribution(string s,int n){
	int fruits=0;
	if (s.length()-n==2) {
	for (int i = 2;i>=1; i--) {
	if (s[i] == 'a') {
fruits++;
}
else if (s[i] == 'o') {
fruits++;
}
else {
fruits++;
}

	return fruits-n;
	}
	}
else return -1;
}
int main(){
char fruit_str[50]; 
cin>>fruit_str;
int n=atoi(fruit_str);
if (n==1) {
cout<<"there is no mango in the basket\n";
return 0;

}
	else if (n>=2 && n<=3){
for (int i = 1;i<4; i++) {
if (fruit_str[i] == 'm') {
cout<<"there is one mango in the basket\n";
break;}
}}
}
return 0