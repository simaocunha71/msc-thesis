    int count = 0;
    for (char c : num) {
        if (c >= '2' && c <= '7' || c == 'B' || c == 'D' || c == 'F') {
            count++;
        }
    }
    return count;
}
//This function takes a string as input and returns an integer.
//This function counts the number of hexadecimal digits that are prime (2,3,5,7,B,D,F) in the given string.
//It iterates over each character in the string and checks if it is prime by comparing it to the conditions specified.
//If it is prime, it increments the count. Finally, it returns the count.
//This function assumes that the input string is correct and does not contain any lowercase letters or any characters other than the hexadecimal digits.