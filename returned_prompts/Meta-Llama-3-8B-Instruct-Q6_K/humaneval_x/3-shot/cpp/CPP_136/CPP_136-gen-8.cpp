    int max_negative = 0;
    int min_positive = INT_MAX;
    for (int i : lst) {
        if (i < 0 && i > max_negative) {
            max_negative = i;
        }
        if (i > 0 && i < min_positive) {
            min_positive = i;
        }
    }
    return {max_negative, min_positive};
}
