    // Check if date string is not empty
    if (date.empty())
        return false;

    // Check if date is in correct format
    if (date[2] != '-' || date[5] != '-')
        return false;

    // Extract month, day and year from date string
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    // Convert month, day and year to integer
    int m = stoi(month);
    int d = stoi(day);
    int y = stoi(year);

    // Check if month is valid
    if (m < 1 || m > 12)
        return false;

    // Check if day is valid for each month
    if ((m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) && (d < 1 || d > 31))
        return false;
    else if ((m == 4 || m == 6 || m == 9 || m == 11) && (d < 1 || d > 30))
        return false;
    else if (m == 2 && (d < 1 || d > 29))
        return false;

    return true;
}

/*
I: 
The function valid_date takes a string date as input. It checks if the date string is not empty. If it is empty, it returns false.

Next, it checks if the date is in the correct format. If the date is not in the correct format, it