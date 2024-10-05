    int max_negative = INT_MIN, min_positive = INT_MAX;
    for (int i : lst) {
        if (i < 0 && i > max_negative) {
            max_negative = i;
        }
        if (i > 0 && i < min_positive) {
            min_positive = i;
        }
    }
    return {(max_negative == INT_MIN) ? 0 : max_negative,
            (min_positive == INT_MAX) ? 0 : min_positive};
}  // This solution uses INT_MIN and INT_MAX macros from standard library to represent the minimum and maximum integer values. It iterates over the vector and keeps track of the maximum negative and minimum positive integer. If no negative or positive integer is found, it returns 0.