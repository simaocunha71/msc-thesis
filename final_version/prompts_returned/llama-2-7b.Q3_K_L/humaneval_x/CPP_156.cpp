/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == "xix"
>>> int_to_mini_roman(152) == "clii"
>>> int_to_mini_roman(426) == "cdxxvi"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_romank(int number){
	if(number>=1000 || number<=1 ) return NULL;
	int len=0;
	while(true){
		len+=1;
		if((number%10)>5) {
			string ans="";
			for (int i = 6; i <= 10; ++i) {
			    ans=to_string(number/pow(10,8))+ans+"m"+to_string(number%pow(10,8));
			}
			return ans.substr(len-2);
		}else{
			if((number%10)==5){
				int rem=num/power(10,9)+5;
				string ans="";
				for (int i = 0; i <= 4; ++i) {
				    ans=to_string(rem*pow(10,8))+ans+"d"+to_string((rem/power(10,8)));}
				return ans.substr(len-2);
			}else{
				if(number%5>=3){
				int rem=num/pow(10,4)+3;
				string ans="";
				for (int i = 0; i <= 4; ++i) {
				    ans=to_string(rem*pow(10,8))+ans+"x"+