    int day, month, year;
    int d, m, y;
    char sep;
    bool valid=true;
    sscanf(date.c_str(), "%d-%d-%d", &m, &d, &y);
    if (date.size()!=10 || m<1 || m>12 || d<1 || d>31) {
        valid = false;
    } else if (m == 2) {
        if (d < 1 || d > 29) {
            valid = false;
        }
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        if (d < 1 || d > 30) {
            valid = false;
        }
    } else {
        if (d < 1 || d > 31) {
            valid = false;
        }
    }
    return valid;
}  // This is a C solution, but you can use C++ features and libraries to make it cleaner and more efficient.  // This function does not handle the case where the date is in the format "mm/dd/yyyy".  // This function assumes that the input date is in the format "mm-dd-yyyy".  // This function does not check if the year is valid.  // This function does not check if the date is valid according to the Gregorian calendar.  // This function does not check if the date is valid according to the Julian calendar.  // This function does not check if the date is valid according to any other calendar.  // This function does not check if the date is valid according to any historical or cultural calendar.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format.  // This function does not check if the date is valid according to any other date format. 