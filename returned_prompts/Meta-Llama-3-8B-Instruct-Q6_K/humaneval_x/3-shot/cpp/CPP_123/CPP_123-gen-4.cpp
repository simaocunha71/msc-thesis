    vector<int> result;
    int num = n;
    while (num != 1) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        if (num % 2 != 0) {
            result.push_back(num);
        }
    }
    sort(result.begin(), result.end());
    return result;
}  // returns {1, 5}
}  // returns {1, 5}

