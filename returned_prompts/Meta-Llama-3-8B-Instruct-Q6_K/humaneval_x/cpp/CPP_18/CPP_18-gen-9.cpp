    int count = 0;
    size_t pos = 0;
    while ((pos = str.find(substring, pos)) != string::npos) {
        pos += substring.length();
        count++;
    }
    return count;
}
