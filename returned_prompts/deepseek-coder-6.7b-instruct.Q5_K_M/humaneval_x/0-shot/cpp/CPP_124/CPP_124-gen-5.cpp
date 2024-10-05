    if (date.size() != 10 || date[2] != '-' || date[5] != '-')
        return false;

B:
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    for (int i = 0; i < 2; i++)
        if (!isdigit(month[i]))
            return false;

    for (int i = 0; i < 2; i++)
        if (!isdigit(day[i]))
            return false;

    for (int i = 0; i < 4; i++)
        if (!isdigit(year[i]))
            return false;

C:
    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    if (m < 1 || m > 12 || d < 1 || y < 1)
        return false;

D:
    if (m == 2){
        if(d > 29)
            return false;
    }
    else if (m == 4 || m == 6 || m == 9 || m == 11){
        if(d > 30)
            return false;
    }
    else if (d > 31)
        return false;

E:
    return true;
}

int main(){
    printf("%d",valid_date("03-11-2000"));
    printf("%d",valid_date("15-01-2012"));
    printf("%d",valid_date("04-0-2040"));
    printf("%d",valid_date("06-04-2020"));
    printf("%d",valid_date("06/04/2020"));
    return 0;
}

Note:
The function valid_date takes in a string date, then checks if the string is in the correct format mm-dd-yyyy. If it isn't, it returns false.

Next, it splits the string into the month