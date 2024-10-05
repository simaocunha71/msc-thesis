    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (isupper(c)) {
            sum += int(c);
        }
    }
    return sum;
}


