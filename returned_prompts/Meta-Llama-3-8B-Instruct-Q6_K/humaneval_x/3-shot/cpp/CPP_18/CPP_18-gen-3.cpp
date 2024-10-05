    int count=0;
    int pos=0;
    while ((pos=str.find(substring)) != string::npos) {
        count++;
        pos += substring.length();
    }
    return count;
}  // This function counts the occurrences of a substring in a string, including overlapping cases.