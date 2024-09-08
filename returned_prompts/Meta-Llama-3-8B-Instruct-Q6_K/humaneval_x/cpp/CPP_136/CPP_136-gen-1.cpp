    vector<int> result;
    int max_negative = INT_MIN;
    int min_positive = INT_MAX;

    for (int num : lst) {
        if (num < 0 && num > max_negative) {
            max_negative = num;
        }
        if (num > 0 && num < min_positive) {
            min_positive = num;
        }
    }

    if (max_negative == INT_MIN) {
        result.push_back(0);
    } else {
        result.push_back(max_negative);
    }

    if (min_positive == INT_MAX) {
        result.push_back(0);
    } else {
        result.push_back(min_positive);
    }

    return result;
}

