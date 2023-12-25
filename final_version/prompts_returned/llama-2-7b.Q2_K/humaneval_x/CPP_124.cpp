/*
You have to write a function which validates a given date string and
returns true if the date is valid otherwise false.
The date is valid if all of the following rules are satisfied:
1. The date string is not empty.
2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
3. The months should not be less than 1 or higher than 12.
4. The date should be in the format: mm-dd-yyyy

for example: 
valid_date("03-11-2000") => true

valid_date("15-01-2012") => false

valid_date("04-0-2040") => false

valid_date("06-04-2020") => true

valid_date("06/04/2020") => false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool valid_date(string date){
	int n,m,y;
	n= m = y  = atoi(date.c_str());
	for (int i=31 ;i>=0 && i<=12 ;++i) if (n==0 || n>i ) return false ;
	for ( int j=0 ;j<12;++j) if (m==0 || m>j|| m!=j+1 ) return false ;
	for(int k=0;k<=31;k++) if(y==0 || y>k || y>365 )return false ;
	if((date[2] == '-') && (date[4] == '-')){
		for(n = atoi(&date[6]); n<1;++n) return false;}
	else if ((date[0] != '-') || date[1]!=31||date[2].