    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result = "";
    for (size_t i = 0; i < values.size(); ++i) {
        while (number >= values[i]) {
            number -= values[i];
            result += numerals[i];
        }
    }
    return result;
}


