    if(date.size() != 10 || date[2] != '-' || date[5] != '-')
        return false;
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    if(stoi(month) < 1 || stoi(month) > 12)
        return false;
    if((stoi(month) == 4 || stoi(month) == 6 || stoi(month) == 9 || stoi(month) == 11) && (stoi(day) < 1 || stoi(day) > 30))
        return false;
    if(stoi(month) == 2 && (stoi(day) < 1 || stoi(day) > 29))
        return false;
    if((stoi(month) != 2 && (stoi(day) < 1 || stoi(day) > 31)) || (stoi(month) == 2 && stoi(day) > 28))
        return false;
    return true;
}

int main(){
    printf("%d\n", valid_date("03-11-2000")); // true
    printf("%d\n", valid_date("15-01-2012")); // false
    printf("%d\n", valid_date("04-0-2040"));  // false
    printf("%d\n", valid_date("06-04-2020")); // true
    printf("%d\n", valid_date("06/04/2020")); // false
    return 0;
}

Note: This solution assumes that the date is not a leap year. If the date is a leap year, the maximum number of days for February is 29, not 28.
*/

/*
