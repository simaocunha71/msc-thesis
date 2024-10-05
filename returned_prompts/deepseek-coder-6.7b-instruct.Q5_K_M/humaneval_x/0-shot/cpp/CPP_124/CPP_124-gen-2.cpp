    if(date.length() != 10) return false;
    if(date[2] != '-' || date[5] != '-') return false;

B:
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    if(m < 1 || m > 12 || d < 1 || y < 1) return false;

C:
    if(m == 2){
        if(d > 29) return false;
    }
    else if(m == 4 || m == 6 || m == 9 || m == 11){
        if(d > 30) return false;
    }
    else{
        if(m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12){
            if(d > 31) return false;
        }
    }

D:
    return true;
}
int main()
{
    printf(valid_date("03-11-2000") ? "true" : "false");
    printf(valid_date("15-01-2012") ? "true" : "false");
    printf(valid_date("04-0-2040") ? "true" : "false");
    printf(valid_date("06-04-2020") ? "true" : "false");
    printf(valid_date("06/04/2020") ? "true" : "false");

    return 0;
}

The program first checks if the length of the string is 10 and if the string follows the mm-dd-yyyy format. If not, it returns false.
The program then splits the date into month, day, and year and converts them to integers. If any of these are less than 1 or greater than their respective maximum values, it returns false.
In the next step, the program