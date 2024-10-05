    int sum = 0, binary = N;
    string result = "";
    while (binary > 0) {
        sum += binary % 2;
        result = (binary % 2 == 1 ? "1" : "0") + result;
        binary /= 2;
    }
    return result;
}   



