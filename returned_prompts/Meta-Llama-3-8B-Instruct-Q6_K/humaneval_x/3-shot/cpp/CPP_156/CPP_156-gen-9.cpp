    vector<pair<int, string>> roman_nums = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};
    string roman_num_str = "";
    for (int i = 0; i < roman_nums.size(); i++) {
        while (number >= roman_nums[i].first) {
            number -= roman_nums[i].first;
            roman_num_str += roman_nums[i].second;
        }
    }
    return roman_num_str;
}