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
	if(date.length()==0)return false;
    int x=1,y=31;
    if(std::to_lower(date[0]) == 'm'){x=32;}
    else if(std::to_lower(date[0]) == 'a' || std::to_lower(date[0]) == 'A'){x=7;y=31;}
    else if(std::to_lower(date[0]) == 'f'){y=29;}
    int days = stoi(date.substr(2, 4));
	int month = stoi(date.substr(5,2))-x;
	if((month >=1 && month<=12)&& (days>=1 && days <= y)){
		return true;
	}else{ return false;}
}
