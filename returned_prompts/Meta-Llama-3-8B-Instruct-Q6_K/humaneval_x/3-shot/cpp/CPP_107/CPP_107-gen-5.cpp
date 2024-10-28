    vector<int> result;
    int even = 0, odd = 0;
    for (int i = 1; i <= n; i++) {
        string s = to_string(i);
        if (s == reverse(s)) {
            if (i % 2 == 0)
                even++;
            else
                odd++;
        }
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}