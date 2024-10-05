    if (date.empty()){
        return false;
    }
    if (date.size() != 10){
        return false;
    }
    if (date[2] != '-'){
        return false;
    }
    if (date[5] != '-'){
        return false;
    }
    int month = atoi(date.substr(0,2).c_str());
    int day = atoi(date.substr(3,2).c_str());
    int year = atoi(date.substr(6,4).c_str());
    if (month < 1 || month > 12){
        return false;
    }
    if (month == 2 && day > 29){
        return false;
    }
    if (month == 4 || month == 6 || month == 9 || month == 11){
        if (day < 1 || day > 30){
            return false;
        }
    }
    if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
        if (day < 1 || day > 31){
            return false;
        }
    }
    return true;
}

int main(){
    string date1 = "03-11-2000";
    string date2 = "15-01-2012";
    string date3 = "04-0-2040";
    string date4 = "06-04-2020";
    string date5 = "06/04/2020";
    printf("%d\n",valid_date(date1));
    printf("%d\n",valid_date(date2));
    printf("%d\n",valid_date(date3));
    printf("%d\n",valid_date(date4));
    printf("%d\n",valid_date(date5));
    return 0;
}


























