    vector<int> y;
    int i, j, digit;
    bool has_even_digit;
    for (i = 0; i < x.size(); i++) {
        has_even_digit = false;
        j = x[i];
        while (j > 0) {
            digit = j % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            j = j / 10;
        }
        if (!has_even_digit) {
            y.push_back(x[i]);
        }
    }
    sort(y.begin(), y.end());
    return y;
}

