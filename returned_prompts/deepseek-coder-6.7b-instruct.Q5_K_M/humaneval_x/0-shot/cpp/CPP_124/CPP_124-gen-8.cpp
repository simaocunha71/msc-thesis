    // Check if the date is not empty
    if (date.empty())
        return false;

    // Check if the date is in the correct format
    if (date[2] != '-' || date[5] != '-' || date.size() != 10)
        return false;

    // Extract month, day and year from the date
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    // Convert string to int
    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    // Check if the values are valid
    if (m < 1 || m > 12 || d < 1 || y < 1)
        return false;

    // Check for the number of days in a month
    if (m == 2){
        if (d > 29)
            return false;
    }
    else if (m == 4 || m == 6 || m == 9 || m == 11){
        if (d > 30)
            return false;
    }
    else{
        if (m == 2){
            if (d > 28)
                return false;
        }
        else if (d > 31)
            return false;
    }

    return true;
}

int main(){
    printf("%d\n",valid_date("03-11-2000"));
    printf("%d\n",valid_date("15-01-2012"));
    printf("%d\n",valid_date("04-0-2040"));
    printf("%d\n",valid_date("06-04-2020"));
    printf("%d\n",valid_date("06/04/2020"));
    return 0;
}

This code is written in C++. It first checks if the date is not empty and if it's in the correct format (mm-dd-yyyy). Then it extracts the month, day, and year from the