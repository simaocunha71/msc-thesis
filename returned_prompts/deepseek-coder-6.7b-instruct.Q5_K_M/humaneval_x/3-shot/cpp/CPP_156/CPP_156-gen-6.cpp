    string rom[] = {"", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"};
    string tho[] = {"", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"};
    string hun[] = {"", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"};
    string thou[] = {"", "m", "mm", "mmm"};

    string result = "";
    result += thou[number/1000];
    result += hun[(number%1000)/100];
    result += tho[(number%100)/10];
    result += rom[number%10];

    return result;
}


