    vector<int> result;
    int even = 0, odd = 0;
    string str = to_string(num);
    for (int i = 0; i < str.length(); i++) {
        if (str[i] - '0' % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}