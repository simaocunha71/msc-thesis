    if(base < 2 || base > 9) {
        return "base should be between 2 and 9";
    }
    string res = "";
    while(x > 0) {
        res = (char)(x % base + '0') + res;
        x /= base;
    }
    return res;
}

