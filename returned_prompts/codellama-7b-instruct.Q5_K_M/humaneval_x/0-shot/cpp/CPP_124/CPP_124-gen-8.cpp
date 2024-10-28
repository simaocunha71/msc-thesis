
    if(date.empty()){
        return false;
    }

    int month = stoi(date.substr(0,2));
    int day = stoi(date.substr(3,2));
    int year = stoi(date.substr(6,4));

    // month
    if(month < 1 || month > 12){
        goto A;
    }

    // day
    if(day < 1 || day > 31){
        goto A;
    }

    // year
    if(year < 1){
        goto A;
    }

    return true;
}

int main(){

    string date;
    cout << "Enter a date (mm-dd-yyyy): ";
    cin >> date;

    if(valid_date(date)){
        cout << "Valid date!" << endl;
    }else{
        cout << "Invalid date!" << endl;
    }

    return 0;
}
