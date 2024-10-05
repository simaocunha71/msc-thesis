    int apples = 0, oranges = 0;
    stringstream ss(s);
    string temp;
    while (!ss.eof()) {
        ss >> temp;
        if (stringstream(temp) >> apples) continue;
        if (temp == "apples") continue;
        if (stringstream(temp) >> oranges) continue;
        if (temp == "oranges") continue;
    }
    return n - apples - oranges;
}


