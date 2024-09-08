    // Write your code here
    if(date.empty()) return false;
    size_t space = date.find('-');
    if(space == string::npos) return false;
    string month = date.substr(0, space);
    string day = date.substr(space+1, space-space-1);
    string year = date.substr(space+2);
    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);
    if(m < 1 || m > 12) return false;
    if(y <= 0) return false;
    if(m == 2){
        if(d < 1 || d > 29) return false;
    }else if(m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12){
        if(d < 1 || d > 31) return false;
    }else if(m == 4 || m == 6 || m == 9 || m == 11){
        if(d < 1 || d > 30) return false;
    }
    return true;
}