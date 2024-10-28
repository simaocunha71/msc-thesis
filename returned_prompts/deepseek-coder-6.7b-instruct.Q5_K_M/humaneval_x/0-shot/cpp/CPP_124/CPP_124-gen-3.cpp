    if(date.empty()) return false;

B:
    if(date[2] != '-' || date[5] != '-') return false;

C:
    int month = stoi(date.substr(0,2));
    int day = stoi(date.substr(3,2));
    int year = stoi(date.substr(6,4));

    if(month < 1 || month > 12) return false;

D:
    if(month == 4 || month == 6 || month == 9 || month == 11){
        if(day < 1 || day > 30) return false;
    }else if(month == 2){
        if(day < 1 || day > 29) return false;
    }else{
        if(day < 1 || day > 31) return false;
    }

E:
    return true;

}



int main(){
    printf("%s\n", valid_date("03-11-2000") ? "true" : "false");
    printf("%s\n", valid_date("15-01-2012") ? "true" : "false");
    printf("%s\n", valid_date("04-0-2040") ? "true" : "false");
    printf("%s\n", valid_date("06-04-2020") ? "true" : "false");
    printf("%s\n", valid_date("06/04/2020") ? "true" : "false");
}
```

In this code, function `valid_date` takes a string as an argument and checks the following conditions:

A: If the string is empty, it returns false.

B: If the date string does not contain a '-' character at the 3rd and 6th positions, it returns false.

C: It extracts the month, day, and year from the date string. If any of these values are less than 1 or greater than their respective maximums (as specified in the problem), it returns false.

D: If the month is one of the months with 30 days, it