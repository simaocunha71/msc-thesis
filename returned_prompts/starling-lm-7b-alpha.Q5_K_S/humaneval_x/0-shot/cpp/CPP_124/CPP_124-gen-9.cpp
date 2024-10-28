    if(date.length() == 10 && date[2] == '-' && date[5] == '-'){
        int month = (date[0] - '0') * 10 + (date[1] - '0');
        int day = (date[3] - '0') * 10 + (date[4] - '0');
        int year = (date[6] - '0') * 1000 + (date[7] - '0') * 100 + (date[8] - '0') * 10 + (date[9] - '0');
        if(month == 0 || month == 13 || month > 12 || day == 0 || day > 31 || day > 30 || day > 29 || year == 0){
            return false;
        }
        if(month == 2 && day == 30 || month == 1 && day == 32 || month == 4 && day == 31 || month == 6 && day == 31 || month == 9 && day == 31 || month == 11 && day == 31){
            return false;
        }
        return true;
    }
    return false;
}
int main(){
    string date;
    cin >> date;
    if(valid_date(date)){
        cout << "true";
    }else{
        cout << "false";
    }
}


*/




































































































































































