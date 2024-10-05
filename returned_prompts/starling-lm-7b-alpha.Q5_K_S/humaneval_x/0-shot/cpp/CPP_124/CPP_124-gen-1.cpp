    if(date.length()!=10)
        return false;
    int month = (date[3] - '0') * 10 + (date[4] - '0');
    int day = (date[6] - '0') * 10 + (date[7] - '0');
    int year = (date[9] - '0') * 1000 + (date[10] - '0') * 100 + (date[11] - '0') * 10 + (date[12] - '0');
    if(year < 1900 || year > 9999)
        return false;
    if(month < 1 || month > 12)
        return false;
    if(month == 2){
        if(day < 1 || day > 29)
            return false;
    }
    if(month == 4 || month == 6 || month == 9 || month == 11){
        if(day < 1 || day > 30)
            return false;
    }
    if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
        if(day < 1 || day > 31)
            return false;
    }
    return true;
}
int main(){
    string date;
    cin>>date;
    printf("%d\n",valid_date(date));
    return 0;
}

*/













































































































































