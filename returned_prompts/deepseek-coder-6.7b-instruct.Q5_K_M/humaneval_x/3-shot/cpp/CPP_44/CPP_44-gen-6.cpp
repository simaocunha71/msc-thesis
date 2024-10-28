    string s = "";
    while (x > 0) {
        s = to_string(x % base) + s;
        x /= base;
    }
    return s;
}


