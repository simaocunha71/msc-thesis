    int num = 1;
    string binary = "db";
    while (num <= decimal){
        num *= 2;
        if (num <= decimal){
            binary += "0";
        }
        else {
            binary += "1";
        }
    }
    binary += "db";
    return binary;
}
