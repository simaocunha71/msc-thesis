    int count = 0;
    for (int i = 0; i < s.length(); i += 2) {
        if (isupper(s[i]) && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')) {
            count++;
        }
    }
    return count;
}



