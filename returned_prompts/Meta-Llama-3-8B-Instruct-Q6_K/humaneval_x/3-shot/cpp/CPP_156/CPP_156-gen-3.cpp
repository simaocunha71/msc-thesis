    vector<pair<int, string>> roman_numerals = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};
    string result = "";
    for (int i = 0; i < roman_numerals.size(); i++) {
        while (number >= roman_numerals[i].first) {
            number -= roman_numerals[i].first;
            result += roman_numerals[i].second;
        }
    }
    return result;
}