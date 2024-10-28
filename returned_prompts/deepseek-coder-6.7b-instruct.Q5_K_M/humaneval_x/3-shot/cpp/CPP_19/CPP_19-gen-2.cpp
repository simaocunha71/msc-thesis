    map<string, int> num_dict = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    multimap<int, string> sorted_nums;
    string temp = "";
    string result = "";
    for (char &c : numbers) {
        if (c == ' ') {
            sorted_nums.insert({num_dict[temp], temp});
            temp = "";
        } else {
            temp += c;
        }
    }
    if (!temp.empty()) {
        sorted_nums.insert({num_dict[temp], temp});
    }
    for (auto it = sorted_nums.begin(); it != sorted_nums.end(); ++it) {
        result += it->second + " ";
    }
    return result.substr(0, result.size()-1); // remove trailing space
}

