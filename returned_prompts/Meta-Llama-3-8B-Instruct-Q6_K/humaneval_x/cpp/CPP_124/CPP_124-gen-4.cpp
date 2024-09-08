    int month,day,year;
    // Split the date string into month, day and year
    string delimiter = "-";
    size_t pos = 0;
    string token;
    while ((pos = date.find(delimiter)) != stdstring::npos) {
        token = date.substr(0, pos);
        date.erase(0, pos + delimiter.length());
    }
    month = stoi(token);
    token = date;
    pos = token.find(delimiter);
    day = stoi(token.substr(0, pos));
    token.erase(0, pos + delimiter.length());
    year = stoi(token);

    // Check the month
    if(month<1 || month>12){
        return false;
    }

    // Check the day
    if((month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) && day<1 || day>31){
        return false;
    }
    else if((month==4 || month==6 || month==9 || month==11) && day<1 || day>30){
        return false;
    }
    else if(month==2 && (day<1 || day>29)){
        return false;
    }

    // Check the year
    if(year<1000 || year>9999){
        return false;
    }

    // If all checks pass, the date is valid
    return true;
}

int main(){
    cout<<valid_date("03-11-2000")<<endl;
    cout<<valid_date("15-01-2012")<<endl;
    cout<<valid_date("04-0-2040")<<endl;
    cout<<valid_date("06-04-2020")<<endl;
    return 0;
}
*/



C++ Solution:

```cpp
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool valid_date(string date) {
    int month, day, year;
    stringstream ss(date);
    char ch;
    ss >> month >> ch >> day >> ch >> year;

    if (ss.fail() || ch != '-') {
        return false;
    }

    if (month < 1 || month > 12) {
        return false;
    }

    if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31