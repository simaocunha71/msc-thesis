    string res = "";
    while (x > 0) {
        int r = x % base;
        res = to_string(r) + res;
        x /= base;
    }
    return res;
} // This function works for bases less than 10


