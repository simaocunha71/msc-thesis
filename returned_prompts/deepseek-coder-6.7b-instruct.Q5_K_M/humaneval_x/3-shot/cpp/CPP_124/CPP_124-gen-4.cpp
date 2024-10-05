    if(date.length() != 10)
        return false;
    if(date[2] != '-' || date[5] != '-')
        return false;
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    if(stoi(month) < 1 || stoi(month) > 12)
        return false;
    if(stoi(day) < 1 || stoi(day) > 31)
        return false;
    if((stoi(month) == 4 || stoi(month) == 6 || stoi(month) == 9 || stoi(month) == 11) && stoi(day) > 30)
        return false;
    if(stoi(month) == 2){
        if(stoi(day) > 29)
            return false;
    }
    return true;
}



