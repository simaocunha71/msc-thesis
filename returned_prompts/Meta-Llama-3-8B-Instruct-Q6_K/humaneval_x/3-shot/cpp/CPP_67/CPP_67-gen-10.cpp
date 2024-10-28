    int total_oranges = 0, total_apples = 0;
    int start = 0;
    while (start < s.length()) {
        if (s[start] == 'a') {
            start = s.find("apples", start);
            if (start != string::npos) {
                start += 7;
                int end = s.find(" and ", start);
                if (end != string::npos) {
                    string apples_str = s.substr(start, end - start);
                    total_apples = stoi(apples_str);
                    start = end + 5;
                } else {
                    string apples_str = s.substr(start);
                    total_apples = stoi(apples_str);
                    start = s.length();
                }
            }
        }
        if (s[start] == 'o') {
            start = s.find("oranges", start);
            if (start != string::npos) {
                start += 8;
                int end = s.find(" and ", start);
                if (end != string::npos) {
                    string oranges_str = s.substr(start, end - start);
                    total_oranges = stoi(oranges_str);
                    start = end + 5;
                } else {
                    string oranges_str = s.substr(start);
                    total_oranges = stoi(oranges_str);
                    start = s.length();
                }
            }
        }
    }
    return n - total_apples - total_oranges;
}


