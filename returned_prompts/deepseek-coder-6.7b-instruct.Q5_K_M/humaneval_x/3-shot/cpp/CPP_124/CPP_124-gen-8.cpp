    if(date.length() != 10 || date[2] != '-' || date[5] != '-')
        return false;

    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    if(m < 1 || m > 12 || d < 1 || y < 1)
        return false;

    if(m == 2){
        if(d > 29 || (d > 28 && y % 4 != 0) || (d > 29 && y % 4 == 0 && y % 100 != 0) || d > 30)
            return false;
    }

    else if(m == 4 || m == 6 || m == 9 || m == 11){
        if(d > 30)
            return false;
    }

    else{
        if(d > 31)
            return false;
    }

    return true;
}


