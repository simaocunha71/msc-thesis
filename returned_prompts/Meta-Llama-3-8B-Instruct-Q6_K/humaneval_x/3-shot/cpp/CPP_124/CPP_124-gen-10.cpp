    int day,month,year;
    if(date.size()!=10) return false;
    if(date[4]! '-' || date[7]! '-') return false;
    day=stoi(date.substr(8,2));
    month=stoi(date.substr(0,2));
    year=stoi(date.substr(3,4));
    if(month<1 || month>12) return false;
    if(month==2) return day>=1 && day<=29;
    if(month==4||month==6||month==9||month==11) return day>=1 && day<=30;
    if(month==1||month==3||month==5||month==7||month==8||month==10||month==12) return day>=1 && day<=31;
    return false;
}
// another solution using regex
#include<regex>
bool valid_date(string date){
    regex pattern("^((01|02|03|04|05|06|07|08|09|10|11|12)-([0-2][0-9]|3[01])-(19|20)[0-9]{2})$");
    return regex_match(date,pattern);
}
// another solution using stringstream
#include<sstream>
bool valid_date(string date){
    stringstream ss(date);
    string month,day,year;
    getline(ss,month,'-');
    getline(ss,day,'-');
    int m=stoi(month),d=stoi(day),y=stoi(year.substr(2));
    if(m<1 || m>12) return false;
    if(m==2) return d>=1 && d<=29;
    if(m==4||m==6||m==9||m==11) return d>=1 && d<=30;
    if(m==1||m==3||m==5||m==7||m==8||m==10||m==12) return d>=1 && d<=31;
    return false;
}
// another solution using boost
#include<boost/algorithm/string.hpp>
#include<boost/date_time.hpp>
bool valid_date(string date){
    boost::gregorian::date d=boost::gregorian::from_string(date);
    return !boost::iequals(date,boost::gregorian::to_string(d));
}  // this is not correct as it will return true for invalid dates
// another solution using chrono
#include<chrono>
bool valid_date(string date){
    chrono::year y=chrono