    int m, d, y;

    // Split the date string into month, day, and year.
    int pos = date.find('-');
    m = stoi(date.substr(0, pos));
    date.erase(0, pos+1);
    pos = date.find('-');
    d = stoi(date.substr(0, pos));
    date.erase(0, pos+1);
    y = stoi(date);

    // Check if the date is valid.
    if (m < 1 || m > 12) {
        return false;
    }

    if (m == 2) {
        if (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)) {
            if (d < 1 || d > 29) {
                return false;
            }
        } else {
            if (d < 1 || d > 28) {
                return false;
            }
        }
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        if (d < 1 || d > 30) {
            return false;
        }
    } else {
        if (d < 1 || d > 31) {
            return false;
        }
    }

    // If the date is valid, return true.
    return true;
}

int main() {
    string date;
    cout << "Enter a date in the format: mm-dd-yyyy ";
    cin >> date;
    if(valid_date(date)) {
        cout << "The date is valid." << endl;
    } else {
        cout << "The date is not valid." << endl;
    }
    return 0;
}*/



