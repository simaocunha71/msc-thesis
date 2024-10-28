    int apples = stoi(s.substr(0, s.find(' ')));
    int oranges = stoi(s.substr(s.find_last_of(' ') + 1));
    return n - apples - oranges;
}

