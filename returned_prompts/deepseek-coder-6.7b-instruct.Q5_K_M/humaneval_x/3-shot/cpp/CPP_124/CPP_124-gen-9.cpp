    if(date.size() != 10 || date[2] != '-' || date[5] != '-') 
        return false;

    int month = stoi(date.substr(0, 2));
    int day = stoi(date.substr(3, 2));
    int year = stoi(date.substr(6, 4));

    if(month < 1 || month > 12 || day < 1 || year < 1) 
        return false;

    if(month == 2){
        if(day > 29 || day < 1) 
            return false;
    }
    else if(month == 4 || month == 6 || month == 9 || month == 11){
        if(day > 30 || day < 1) 
            return false;
    }
    else if(day > 31 || day < 1) 
        return false;

    return true;
}


