    string str = to_string(x);
    int len = str.length();
    shift = shift % len;
    if(shift == 0) return str;
    string res = str.substr(shift) + str.substr(0,shift);
    return res;
}

B:
    int n = x;
    int shift = shift % 10;
    int res = 0;
    while(n > 0) {
        int digit = n % 10;
        n = n / 10;
        res = res * 10 + digit;
    }
    string res_str = to_string(res);
    return res_str;
}

C:
    int x = 123;
    int shift = 2;
    int res = 0;
    int temp = x;
    while(temp > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    temp = res;
    while(shift > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    return to_string(res);

D:
    int n = x;
    int shift = shift % (int)log10(n) + 1;
    int res = 0;
    int temp = n;
    while(temp > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    temp = res;
    while(shift > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    return to_string(res);

E:
    int n = x;
    int shift = shift % (int)log10(n) + 1;
    int res = 0;
    int temp = n;
    while(temp > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    temp = res;
    while(shift > 0) {
        int digit = temp % 10;
        temp = temp / 10;
        res = res * 10 + digit;
    }
    return to_string(res);

F:
    int n = x;
    int shift = shift % (int)log10(n) + 