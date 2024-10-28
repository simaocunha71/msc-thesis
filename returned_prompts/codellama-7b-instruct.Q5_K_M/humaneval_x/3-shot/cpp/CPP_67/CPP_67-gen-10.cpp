    int apples = 0, oranges = 0;
    stringstream ss(s);
    string substr;
    while (getline(ss, substr, ' ')) {
        if (substr == "apples") {
            getline(ss, substr, ' ');
            apples = stoi(substr);
        }
        if (substr == "oranges") {
            getline(ss, substr, ' ');
            oranges = stoi(substr);
        }
    }
    return n - apples - oranges;
}



