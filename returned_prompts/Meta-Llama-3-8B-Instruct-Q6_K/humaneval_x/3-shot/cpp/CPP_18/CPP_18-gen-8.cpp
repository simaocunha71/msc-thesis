    int count = 0;
    int pos = 0;
    while ((pos = str.find(substring, pos)) != string::npos) {
        count++;
        pos += substring.length();
    }
    return count;
}  // This function counts the number of times a substring occurs in a string. It uses the find function of the string class and increments the count each time the substring is found. It also adjusts the position to continue searching from where the previous occurrence ended. The function returns the total count.