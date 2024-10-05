    int month,day,year;
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if(date.length() != 10 || date[2] != '-' || date[5] != '-' || month > 12 || month < 1 || day > 31 || day < 1 || year < 1){
        return false;
    }
    if(month == 2 && day > 29){
        return false;
    }
    if((month == 4 || month == 6 || month == 9 || month == 11) && day > 30){
        return false;
    }
    if(month == 2 && day > 28 && year % 4 != 0){
        return false;
    }
    return true;
}


