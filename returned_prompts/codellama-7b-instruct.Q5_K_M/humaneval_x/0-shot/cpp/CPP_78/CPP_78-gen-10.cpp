    if (num.length() == 0) return 0;
    int len = num.length();
    int count = 0;
    int i = 0;
    while (i < len) {
        int tmp = num[i] - 'A' + 11;
        int j = i + 1;
        while (j < len) {
            if (tmp == num[j] - 'A' + 11) {
                break;
            }
            j++;
        }
        if (j == len) {
            count++;
        }
        i = j;
    }
    return count;
}

