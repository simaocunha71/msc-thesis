    // Write your code here
    int day,month,year;
    char c;
    int i=0;
    while(date[i] != '-'){
        month = month * 10 + (date[i] - '0');
        i++;
    }
    i++;
    while(date[i] != '-'){
        day = day * 10 + (date[i] - '0');
        i++;
    }
    i++;
    while(i<date.length()){
        year = year * 10 + (date[i] - '0');
        i++;
    }
    if(month > 12 || day > 31 || (month == 2 && day > 29) || (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 || day < 1){
        return false;
    }
    else if(month < 1 || month > 12 || day < 1 || day > 31){
        return false;
    }
    else
        return true;
}

int main(){
    string date;
    cout<<"Enter date in mm-dd-yyyy format: ";
    cin>>date;
    if(valid_date(date))
        cout<<"The date is valid."<<endl;
    else
        cout<<"The date is not valid."<<endl;
    return 0;
}
