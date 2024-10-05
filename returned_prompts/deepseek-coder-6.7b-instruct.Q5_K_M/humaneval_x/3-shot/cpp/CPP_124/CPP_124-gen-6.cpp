    int m,d,y;
    string delimiter = "-";
    size_t pos = 0;
    string token;
    int month[12] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (date.empty())
        return false;

    while ((pos = date.find(delimiter)) != string::npos) {
        token = date.substr(0, pos);
        m = stoi(token);
        date.erase(0, pos + delimiter.length());
        pos = date.find(delimiter);
        token = date.substr(0, pos);
        d = stoi(token);
        date.erase(0, pos + delimiter.length());
        y = stoi(date);
    }

    if (m < 1 || m > 12 || d < 1 || d > month[m-1] || y < 1)
        return false;

    return true;
}


